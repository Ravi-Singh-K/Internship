from userapp.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.db.models import F
import string
from datetime import timedelta
from .choices import *


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


class BookAssignmentSerializer(serializers.ModelSerializer):
    must_return_within = serializers.SerializerMethodField(read_only=True)
    returned_at = serializers.DateField(required=False)

    class Meta:
        model = BookAssignment
        fields = ['id', 'faculty', 'users', 'book', 'assigned_at', 'must_return_within', 'returned_at', 'status', 'overdue_charge']
        extra_kwargs = {
            'overdue_charge': {
                'read_only': True
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
            book.status = NOT_AVAILABLE  # 'Not Available' is at index 1
            book.save()
        
        return BookAssignment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Retrieve new status and book from the validated data
        status = validated_data.get('status', instance.status)
        book = validated_data.get('book', instance.book)
        returned_at = validated_data.get('returned_at', instance.returned_at)
        overdue_charge = validated_data.get('overdue_charge', instance.overdue_charge)
        assigned_at = validated_data.get('assigned_at', instance.assigned_at)

        must_return_within = assigned_at + timedelta(days=30)
        # breakpoint()

        # If the status is 'Returned', increment the book count
        if status == RETURNED:
            book.book_count = F('book_count') + 1
            book.status = AVAILABLE
            book.save()
            book.refresh_from_db()
        
        if status == PENDING:
            returned_at = None
        
        if returned_at == None:
            status = PENDING

        if returned_at and status == RETURNED:
            if returned_at > must_return_within:
                late_days = (returned_at - must_return_within).days
                overdue_charge = late_days * 100
                instance.overdue_charge = overdue_charge
            else:
                overdue_charge = 0
                instance.overdue_charge = overdue_charge

        else:
            overdue_charge = 0
            instance.overdue_charge = overdue_charge


        # Update the instance with the new data
        instance.status = status
        instance.returned_at = returned_at
        instance.book = book
        instance.save()

        return instance

    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']

        if request and request.method in ['POST', 'PUT', 'PATCH'] and not self.context.get('is_action', False):
            fields.pop('status', None)
            fields.pop('returned_at', None)
        
        if request and request.method == 'GET':
            # Remove 'users' fields from Nested Serializer
            fields['faculty'] = FacultyDisplaySerializer()
            if 'users' in fields['faculty'].fields:
                fields['faculty'].fields.pop('users')

            # Nested Serializer
            fields['users'] = UserDisplaySerializer()

            # Remove fields from UserDisplaySerializer
            if 'primary_group' in fields['users'].fields:
                fields['users'].fields.pop('primary_group')
            if 'faculty' in fields['users'].fields:
                fields['users'].fields.pop('faculty')

            # Remove 'status', 'book_count', 'faculty' from nested serializer
            fields['book'] = BookDisplaySerializer()
            if 'status' in fields['book'].fields:
                fields['book'].fields.pop('status')
            if 'book_count' in fields['book'].fields:
                fields['book'].fields.pop('book_count')
            if 'faculty' in fields['book'].fields:
                fields['book'].fields.pop('faculty')

        return fields

    def validate(self, data):
        # breakpoint()
        faculty = data.get('faculty')
        users = data.get('users')
        book = data.get('book')
        returned_at = data.get('returned_at')
        status = data.get('status')

        if status == RETURNED and returned_at == None:
            raise serializers.ValidationError({"Returned_at" : "You must specify returned_at if status is 'returned'."})
        elif status == PENDING and returned_at != None:
            raise serializers.ValidationError({"status" : "Status cannot be 'pending' if returned_at is given."})

        if self.instance:
            assigned_at = self.instance.assigned_at

        if returned_at:
            if returned_at < assigned_at:
                raise serializers.ValidationError({"returned_at" : "The return date cannot be before assigned date."})

        if users is None:
            raise serializers.ValidationError({"users": "User information is missing."})
        if faculty is None:
            raise serializers.ValidationError({"faculty": "Faculty information is missing."})
    
        # Validate that the user belongs to the specified faculty
        if users.faculty != faculty:
            raise serializers.ValidationError({
                "users": "User '{}' does not belong to the faculty '{}'".format(users.username, faculty.name)
            })

        # Validate the given faculty belongs to the assigned faculties of the book instance
        if faculty not in book.faculty.all():
            raise serializers.ValidationError({
                "faculty": "Book '{}' does not belong to the faculty '{}'".format(book.name, faculty.name)
            })

        request = self.context.get('request')
        if request.method == 'POST':
            if book.status == 'Not Available' or book.book_count == 0:
                raise serializers.ValidationError({
                    "book": "The book '{}' is not available to assign.".format(book.name)
                })

        return data
    

class RequestBookSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    # faculty = serializers.PrimaryKeyRelatedField(queryset = Faculty.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset = Faculty.objects.all())

    class Meta:
        model = RequestBook
        fields = ('id', 'book', 'requested_at')
        extra_kwargs = {
            'requested_at': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # self.fields['user'].queryset = CustomUser.objects.filter(id=request.user.id)
            # self.fields['faculty'].queryset = Faculty.objects.filter(name = request.user.faculty)
            self.fields['book'].queryset = Book.objects.filter(faculty = request.user.faculty)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']
        if request and request.method == 'GET':

            # user_serializer = UserDisplaySerializer()
            # user_serializer.fields = {"first_name": user_serializer.fields['first_name']}
            # fields['user'] = user_serializer

            # faculty_serializer = FacultyDisplaySerializer()
            # faculty_serializer.fields = {"name": faculty_serializer.fields['name']}
            # fields['faculty'] = faculty_serializer

            book_serializer = BookDisplaySerializer()
            for field in ['id', 'status', 'book_count', 'faculty']:
                book_serializer.fields.pop(field, None)
            fields['book'] = book_serializer

            fields['user'] = UserDisplaySerializer()
            for field in ['id', 'faculty', 'address']:
                fields['user'].fields.pop(field, None)

            fields['faculty'] = FacultyDisplaySerializer()
            for field in ['id', 'users']:
                fields['faculty'].fields.pop(field, None)

        return fields
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        validated_data['faculty'] = self.context.get('request').user.faculty
        return RequestBook.objects.create(**validated_data)