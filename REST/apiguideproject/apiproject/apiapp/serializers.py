
# from rest_framework import serializers
# from .models import Movie, MOVIE_GENRE, MOVIE_LANGUAGE
# from django.contrib.auth.models import User
# from rest_framework.exceptions import ValidationError



# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False, allow_blank = True, max_length = 50)
#     owner = serializers.ReadOnlyField(source = 'owner.username')
#     genre = serializers.ChoiceField(choices=MOVIE_GENRE, default = 'Action')
#     language = serializers.ChoiceField(choices=MOVIE_LANGUAGE, default = 'Eng')
#     release_date = serializers.DateField(format="%Y-%m-%d", required = False)
#     description = serializers.CharField(style={'base_template' : 'textarea.html'}, required = False)

#     # extra_kwargs = {
#     #     'release_date' : {'required' : False},
#     #     'description' : {'required' : False}
#     # }

#     def create(self, validated_data):
#         """
#             Create and return a new 'Movie' instance, given the validated data.
#         """
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#             Update and return an existing 'Movie' instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.language = validated_data.get('language', instance.language)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
    

# Using ModelSerializer

# import datetime
# class MovieDisplaySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'genre']


# class MovieSerializer(serializers.ModelSerializer):
#     movie_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = ['movie_name', 'genre', 'language', 'release_date', 'description']
#         # depth = 1   # Displays all the fields of it's depended Model
#         # extra_kwargs = {
#         #     'release_date' : {'write_only' : True},
#         # }

#     def validate(self, data):
#         if data.get('name').lower() == 'hello' or data.get('name').lower() == 'world' or data.get('name').lower() == 'hello world':
#             raise serializers.ValidationError("The Given Name Is Not Allowed.")
        
#         # if 'release_date' in data and data['release_date'] > datetime.date.today:
#         #     raise serializers.ValidationError({'release_date' : 'Release date cannot be in future'})
#         return data
    
#     def get_movie_name(self, obj):
#         return f'{obj.name} {obj.owner.username}'
    

#     # def to_representation(self, instance):
#     #     representation = super().to_representation(instance)
#     #     representation['name'] = instance.name + instance.owner.username
#     #     return representation

    
    
# class UserDisplaySerializer(serializers.ModelSerializer):
#     movies2 = MovieDisplaySerializer(many = True, source = 'movies')

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'movies2']
    

# class UserSerializer(serializers.ModelSerializer):
#     movies1 = MovieSerializer(many = True, source = 'movies')
#     action = serializers.BooleanField(source = 'is_active')

#     class Meta:
#         model = User
#         fields = ['id', 'username','movies1', 'action']




# Customizing Serializer Fields
from rest_framework import serializers
from .models import Movie, MOVIE_GENRE, MOVIE_LANGUAGE
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    # movie_info = MovieSerializer(many = True, source = 'movies')

    class Meta:
        model = User
        fields = ['id', 'username']
    

class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    new_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'language', 'description', 'release_date', 'new_name', 'owner']

    def get_new_name(self, obj):
        return f"{obj.owner} {obj.name}"

    def to_representation(self, value):
        representation = super().to_representation(value)
        representation['owner'] = f'{value.owner.username} {value.owner.id}'
        representation['owner_id'] = self.context.get('user_id')
        return representation

    def get_new_name(self, obj):
        return f"{obj.name}"

    def validate(self, data):
        if data.get('name') == 'ravi':
            raise serializers.ValidationError({
                'name': 'The given name is not allowed. Please provide a genuine movie name.'
            })
        return data

    def get_fields(self):
        fields = super().get_fields()
        print(fields)
        # request = self.context.get('request')
        # if request and request.method == 'GET':
        #     fields['release_date'] = MovieSerializer()
        
        return fields
    

    # def get_owner(self, obj):        # if request and request.method == 'GET':
        #     fields['release_date'] = MovieSerializer()
    #     return obj.owner.username

    # def get_movie_name(self, obj):
    #     return f'{obj.name} {obj.owner.username}'
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get('request')
        
    #     if request:
    #         if request.method == 'GET':
    #             self.fields.pop('description', None)
    #             self.fields.pop('highlighted', None)
    #             self.fields.pop('language', None)
    #         elif request.method == 'POST':
    #             self.fields.pop('id', None)
    #             self.fields.pop('genre', None)
    #             self.fields.pop('language', None)
    #             self.fields.pop('highlighted', None)


        


    


    











# Using HyperLinkedModelSerializer

# class MovieSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source = 'owner.username')
    
#     class Meta:
#         model = Movie
#         fields = ['url', 'id', 'owner', 'name', 'genre', 'language', 'release_date', 'description']

#         def validate_name(self, validated_data):
#             if validated_data["name"] == 'Hello':
#                 raise serializers.ValidationError("Movie name not allowed")

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     movies = serializers.HyperlinkedIdentityField(many = True, view_name="movie-detail", read_only = True)
#     user_movies = MovieSerializer(many = True, source = 'movies')

#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'movies' 'user_movies']