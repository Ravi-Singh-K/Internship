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
from filter_map.backends import FilterMapBackend



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
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'partial_update', 'destroy']:
            permission_classes = [ IsLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticated, IsLibrarian]
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
    queryset = BookAssignment.objects.all()
    serializer_class = BookAssignmentSerializer
    permission_classes = [IsLibrarian]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
