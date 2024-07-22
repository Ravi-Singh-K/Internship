from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserRegistrationSerializer, UserLoginSerializer, BookSerializer, UserDetailSerializer
from .models import *
from rest_framework import permissions, filters, status
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.


class RegistrationViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        return queryset
    
    def get_serializer_class(self):
        return UserRegistrationSerializer
    


from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer

class LoginViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(username=request.data['username'])
            refresh = RefreshToken.for_user(user)
            refresh['id'] = user.id
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginViewSet(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny)
#     serializer_class = CustomTokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         return Response(serializer.validated_data)



class UserDetailViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['first_name']
    search_fields = ['^first_name']
    ordering_fields = ['first_name']


from .filters import *
class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, IsOwnerFilterBackend]
    search_fields = ['^title']
    ordering_fields = ['author']
        
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Book.objects.filter(user_id = user.id)
    #     return queryset

    # def get_permissions(self):
    #     request = self.get_serializer_context()
    #     if request == 'GET':
    #         permission_classes = [permissions.IsAuthenticatedOrReadOnly()]
    #     else:
    #         permission_classes = [permissions.IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()]
    #     return permission_classes
    

class CustomSearchField(filters.SearchFilter):
    
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)
