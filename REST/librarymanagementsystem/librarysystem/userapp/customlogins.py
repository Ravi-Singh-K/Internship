from rest_framework.response import Response
from rest_framework.views import APIView    
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model


class LoginAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, None)  # authentication successful
