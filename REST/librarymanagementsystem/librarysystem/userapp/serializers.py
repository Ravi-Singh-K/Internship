from userapp.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import (authenticate, get_user_model)
from django.contrib.auth.models import Permission
from django.db.models import F
import string
from datetime import datetime, timedelta, date


class FacultyCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ['name']

    def validate_name(self, value):
        if Faculty.objects.filter(name = value).exists():
            raise serializers.ValidationError({'error':'The given name already exists.'})
        if value.isdigit():
            raise serializers.ValidationError({'error':'Faculty cannot be numeric.'})
        if value == ' ':
            raise serializers.ValidationError({'error':'Faculty cannot be empty.'})
        return value
    

class FacultyDisplaySerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'users']

    def get_users(self, obj):
        users = CustomUser.objects.filter(faculty = obj)
        exclude_fields = ['primary_group', 'faculty'] # these fields are passed from UserDisplaySerializer where __init__() describes the logic for excluding fields 
        return UserDisplaySerializer(users, many=True, context=self.context, exclude = exclude_fields).data
    

class GroupCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name']


class GroupDisplaySerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'users']

    def get_users(self, obj):
        users = CustomUser.objects.filter(primary_group=obj)
        exclude_fields = ['primary_group', 'faculty'] # these fields are passed from UserDisplaySerializer where __init__() describes the logic for excluding fields 
        return UserDisplaySerializer(users, many=True, context=self.context, exclude = exclude_fields).data


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'profile_picture', 'first_name', 'last_name', 'username','address', 'contact', 'primary_group', 'faculty', 'email', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'max_length' : 100,
                'required' : True,
                'style' : {
                    'input_type':'password'
                    }
            },
            'username' : {
                'help_text' : None
            },
        }
    
    def validate(self, attrs):
        if CustomUser.objects.filter(username = attrs['username']).exists():
            raise serializers.ValidationError({'error':'Username already exists.'})
        if CustomUser.objects.filter(email = attrs['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists.'})
        
        return attrs
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user


class UserDisplaySerializer(serializers.ModelSerializer):
    primary_group = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'profile_picture', 'first_name', 'last_name', 'address', 'contact', 'primary_group', 'faculty']
    
    def get_primary_group(self, obj):
        if obj.primary_group is not None:
            return obj.primary_group.name
    
    def get_faculty(self, obj):
        if obj.faculty is not None:
            return obj.faculty.name

    def __init__(self, *args, **kwargs): # this __init__ method pops the fields while serializing from other serializer
        exclude = kwargs.pop('exclude', None)
        super(UserDisplaySerializer, self).__init__(*args, **kwargs)
        if exclude:
            for field in exclude:
                self.fields.pop(field)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data
    

class BookCreationSerializer(serializers.ModelSerializer):
    faculty = serializers.SlugRelatedField(
        many = True,
        slug_field='name',
        queryset = Faculty.objects.filter()
    )
    class Meta:
        model = Book
        fields = ['name', 'status', 'book_count', 'faculty']
    
    def validate_name(self, value):
        if Book.objects.filter(name = value).exists():
            raise serializers.ValidationError({'name':'Book already exists.'})
        return value


class BookDisplaySerializer(serializers.ModelSerializer):
    faculty = serializers.SlugRelatedField(many = True, slug_field='name', queryset = Faculty.objects.all())
    class Meta:
        model = Book
        fields = ['id', 'name', 'status', 'book_count', 'faculty']


class AssignmentDisplaySerializer(serializers.ModelSerializer):
    must_return_within = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = BookAssignment
        fields = "__all__"
        extra_kwargs = {
            'overdue_charge' : {
                'read_only' : True
            },
        }

    def get_must_return_within(self, obj):
        return obj.assigned_at + timedelta(days=30)
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']
        if request and request.method == 'GET':

            # Remove 'users' fields from Nested Serializer
            fields['faculty'] = FacultyDisplaySerializer()
            if 'users' in fields['faculty'].fields:
                fields['faculty'].fields.pop('users')

            # Nested Serializer
            fields['users'] = UserDisplaySerializer()

            # Remove fields from UserDisplaySerializer
            if 'primary_group' or 'faculty' in fields['users'].fields:
                fields['users'].fields.pop('primary_group')
                fields['users'].fields.pop('faculty')

            # Remove 'status', 'book_count', 'faculty' from nested seializer
            fields['book'] = BookDisplaySerializer()
            if 'status' or 'book_count' or 'faculty' in fields['book'].fields:
                fields['book'].fields.pop('status')
                # fields['book'].fields.pop('book_count')
                fields['book'].fields.pop('faculty')
        
        return fields


class BookAssignmentSerializer(serializers.ModelSerializer):

    must_return_within = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = BookAssignment
        fields = ['id', 'faculty', 'users', 'book', 'assigned_at', 'must_return_within', 'returned_at', 'status', 'overdue_charge']
        extra_kwargs = {
            'overdue_charge' : {
                'read_only' : True
            },
        }

    def get_must_return_within(self, obj):
        return obj.assigned_at + timedelta(days=30)

    def create(self, validated_data):

        book = validated_data['book']
        
        # Use F expression to handle concurrent updates safely
        book.book_count = F('book_count') - 1
        book.save()
        book.refresh_from_db()  # Refresh the book object to get the updated book_count value

        if book.book_count == 0:
            book.status = BOOK_CHOICES[1][0]  # 'Not Available' is at index 1
            book.save()
        
        return BookAssignment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        # Retrieve new status and book from the validated data
        status = validated_data.get('status', instance.status)
        book = validated_data.get('book', instance.book)


        # If the status is 'Returned', increment the book count
        if status == RETURNED_STATUS_CHOICES[0][0]:
            book.book_count = F('book_count') + 1
            book.save()
            book.refresh_from_db()
        
        # If the book count is greater than 0, update the book's status to 'Available'
        if book.book_count > 0:
            book.status = BOOK_CHOICES[0][0]
            book.save()

        # Update the instance with the new data
        instance.status = status
        instance.book = book
        instance.save()

        return instance

    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']
        if request and request.method == 'GET':

            # Remove 'users' fields from Nested Serializer
            fields['faculty'] = FacultyDisplaySerializer()
            if 'users' in fields['faculty'].fields:
                fields['faculty'].fields.pop('users')

            # Nested Serializer
            fields['users'] = UserDisplaySerializer()

            # Remove fields from UserDisplaySerializer
            if 'primary_group' or 'faculty' in fields['users'].fields:
                fields['users'].fields.pop('primary_group')
                fields['users'].fields.pop('faculty')

            # Remove 'status', 'book_count', 'faculty' from nested seializer
            fields['book'] = BookDisplaySerializer()
            if 'status' or 'book_count' or 'faculty' in fields['book'].fields:
                fields['book'].fields.pop('status')
                # fields['book'].fields.pop('book_count')
                fields['book'].fields.pop('faculty')
        
        return fields

    def validate(self, data):
        """ 
            Convert single instance to a list for iteration otherwise it will throw CustomUser is not iterable 
        """
        faculty = data.get('faculty')
        users = data.get('users')
        book = data.get('book')

        # Ensure users are iterable (e.g., list, queryset)
        # if isinstance(users, CustomUser):
        #     users = [users]  
        
        # Validate each user belongs to the specified faculty
        # for user in users:
        if users.faculty != faculty:
            raise serializers.ValidationError({" Users " : " User '{}' does not belong to the faculty '{}' ".format(users.username, faculty.name)})

        # Validate given faculty belongs to many assigned faculties of book instance
        if faculty not in book.faculty.all():
            raise serializers.ValidationError(f"Book '{book.name}' does not belong to the faculty '{faculty.name}'.")
        
        request = self.context.get('request')
        if request.method == 'POST':
            if book.status == 'Not Available' or book.book_count == 0:
                raise serializers.ValidationError({"book" : "The book '{}' is not available to assign.".format(book.name)})
        
        return data