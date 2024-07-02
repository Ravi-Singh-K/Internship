import string
from .models import Book, GENRE_CHOICE
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserRegistrationSerializer(serializers.ModelSerializer):

    re_password = serializers.CharField(
        min_length = 4,
        write_only = True,
        required = True,
        style = {'input_type' : 'password'}
        )
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 're_password')
        extra_kwargs = {
            'username' : {
                'help_text' : None
            },
            'password' : {
                'style' : {'input_type' : 'password'},
                'write_only' : True,
                'min_length' : 4
            }
        }
    
    def create(self, validated_data):
        validated_data.pop('re_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
    
    def validate(self, data):

        if data['password'] != data['re_password']:
            raise serializers.ValidationError({'Password' : 'Password does not match with each other.'})
        if len(data['password']) < 8:
            raise serializers.ValidationError({'Password' : 'Password must be greater than 8 characters.'})
        if data['password'].isdigit():
            raise serializers.ValidationError({'Password' : 'Password is entirely numeric.'})
        

        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError({'Username' : 'Username already exist.'})
        
        return data
        

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {
            'published_date' : {'format' : '%Y-%m-%d'}
        }
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.first_name
        return representation


class UserDetailSerializer(serializers.ModelSerializer):
    booke = BookSerializer(many = True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id', 'booke']   
    


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        request = self.context.get('request')

        if username and password:
            user = authenticate(request, username = username, password = password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is not active")
            else:
                raise serializers.ValidationError("Invalid Login Credentials")
        else:
            raise serializers.ValidationError("Both Username and Password are required")
        data['user'] = user
        return data