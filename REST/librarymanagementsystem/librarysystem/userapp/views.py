from django.shortcuts import render
from userapp.models import *
from userapp.serializers import *
from userapp.permissions import *
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework import filters
from userapp.choices import *


class UserRegistrationViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.request.user.is_authenticated:
            permission_classes = [NotAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_map = {
            'create' : UserRegistrationSerializer,
            'list' : UserDisplaySerializer,
            'retrieve' : UserDisplaySerializer,
            'update' : UserDisplaySerializer,
            'partial_update' : UserDisplaySerializer,
            'destroy' : UserDisplaySerializer
        }
        return serializer_map[self.action]


class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    
    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        serializer_map = {
            'create' : FacultyCreationSerializer,
            'list' : FacultyDisplaySerializer,
            'retrieve' : FacultyDisplaySerializer,
            'update' : FacultyDisplaySerializer,
            'partial_update' : FacultyDisplaySerializer,
            'destroy' : FacultyDisplaySerializer
        }
        return serializer_map[self.action]
    

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        serializer_map = {
            'create' : GroupCreationSerializer,
            'list' : GroupDisplaySerializer,
            'retrieve' : GroupDisplaySerializer,
            'update' : GroupDisplaySerializer,
            'partial_update' : GroupDisplaySerializer,
            'destroy' : GroupDisplaySerializer
        }
        return serializer_map[self.action]


class AllBookViewSet(ModelViewSet):

    filter_backends = [filters.SearchFilter]
    search_fields = ['^faculty__name']

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and (user.is_superuser or IsLibrarian().has_permission(self.request, self)):
            queryset = Book.objects.all()
        elif user.is_authenticated:
            queryset = Book.objects.filter(faculty=user.faculty)
        else:
            queryset = Book.objects.none()

        return queryset

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'partial_update', 'destroy']:
            permission_classes = [IsLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        serializer_map = {
            'create' : BookCreationSerializer,
            'list' : BookDisplaySerializer,
            'retrieve' : BookDisplaySerializer,
            'update' : BookDisplaySerializer,
            'partial_update' : BookDisplaySerializer,
            'destroy' : BookDisplaySerializer
        }
        return serializer_map[self.action]
    

class JWTLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_200_OK)

class BookAssignmentViewSet(ModelViewSet):
    """
        Create:
        ### Creates an instance of book assignment

        Retrieve
        ### Lists all instances of book assignment

        ### Format

        ```
        javascript
            {
                "id": 1
                "name": "Home Loan2",
                "abbreviation": "HL2",
                "loan_method": {
                    "id": 2,
                    "name": "EMI2",
                    "abbreviation": "E2"
                }
            }
        ```
    """
    serializer_class = BookAssignmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^users__first_name', '^book__name', '^faculty__name']

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and IsLibrarian().has_permission(self.request, self):
            queryset = BookAssignment.objects.all()
        elif user.is_authenticated:
            # queryset = BookAssignment.objects.filter(users__first_name = user.first_name)
            queryset = BookAssignment.objects.filter(users = user.id)
        else:
            queryset = BookAssignment.objects.none()

        return queryset

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'destroy', 'partial_update']:
            permission_classes = [IsLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['get', 'put', 'patch'], serializer_class=BookAssignmentSerializer)
    def set_status(self, request, pk=None):
        book_assignment = self.get_object()

        if request.method == 'GET':
            # Return the current data of the book assignment
            serializer = self.get_serializer(book_assignment)
            return Response(serializer.data)
        serializer = self.get_serializer(book_assignment, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def returned_status(self, request):
        returned_books = self.get_queryset().filter(status=RETURNED)
        serializer = self.get_serializer(returned_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def pending_status(self, request):
        assigned_books = self.get_queryset().filter(status=PENDING)
        serializer = self.get_serializer(assigned_books, many=True)
        return Response(serializer.data)

    def get_serializer(self, *args, **kwargs):
        if self.action in ['set_status', 'returned_status', 'pending_status']:
            kwargs['context'] = {'request': self.request, 'is_action': True}
        return super().get_serializer(*args, **kwargs)
    

class RequestBookViewSet(ModelViewSet):
    queryset = RequestBook.objects.all()
    serializer_class = RequestBookSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.primary_group.name == 'Librarian' or user.is_superuser:
                queryset = RequestBook.objects.all()
            else:
                queryset = RequestBook.objects.filter(faculty=user.faculty)
        else:
            queryset = RequestBook.objects.none()
        return queryset
    
    def get_permissions(self):
        if self.action in ['list', 'update', 'destroy', 'retrieve']:
            permission_classes = [IsLibrarian]
        if self.action in ['list', 'retrieve', 'create']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]