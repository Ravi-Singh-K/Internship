from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = ...

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })



class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'message':'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    # renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(email = email, password = password)
            if user:
                token = RefreshToken.for_user(user)
                return Response({'token':token,'message':'Login Successfull'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileView(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK)



class UserChangePasswordView(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request,format = None):
        serializer = UserChangePasswordSerializer(data = request.data, context = {'user' : request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Changed Successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)