from rest_framework import serializers
from .models import Movie, MOVIE_GENRE, MOVIE_LANGUAGE
from django.contrib.auth.models import User


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
# class MovieSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source = 'owner.username')

#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'genre', 'language', 'release_date', 'description', 'owner']




# class UserSerializer(serializers.ModelSerializer):
#     movies = serializers.PrimaryKeyRelatedField(many = True, queryset = Movie.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'movies']










# Using HyperLinkedModelSerializer

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    
    class Meta:
        model = Movie
        fields = ['url', 'id', 'owner', 'name', 'genre', 'language', 'release_date', 'description']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedIdentityField(many = True, view_name="movie-detail", read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'movies']