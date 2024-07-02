from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserRegistrationSerializer, UserLoginSerializer, BookSerializer, UserDetailSerializer
from .models import *
from rest_framework import permissions, filters
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.


class RegistrationViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_serializer_class(self):
        return UserRegistrationSerializer
    


class LoginViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer_class = UserLoginSerializer
        return serializer_class


class UserDetailViewSet(ModelViewSet):
    queryset = User.objects.all()
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
