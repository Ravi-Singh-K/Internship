# function-based view

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from apiapp.models import Movie
# from apiapp.serializers import MovieSerializer


# @api_view(['GET', 'POST'])
# def movie_list(request, format = None):
#     """
#         List all movies or create a new movie
#     """
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk, format = None):
#     """
#         Retrieve, update or delete a movie.
#     """
#     try:
#         movie = Movie.objects.get(pk = pk)
#     except Movie.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PATCH':
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)








# Class - Based Views

# from apiapp.models import Movie
# from apiapp.serializers import MovieSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class MovieList(APIView):
#     """
#         List all movies or create new movie.
#     """
#     def get(self, request, format = None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format = None):
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class MovieDetail(APIView):
#     """
#         Retrieve, Update or Delete a movie instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Http404
    
#     def get(self, request, pk, format = None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def patch(self, request, pk, format = None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format = None):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)









# Using Mixins

from apiapp.models import Movie
from apiapp.serializers import MovieSerializer, UserSerializer
from rest_framework import mixins, generics, permissions
from django.contrib.auth.models import User
from apiapp.permissions import IsOwnerOrReadOnly


# class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = MovieDisplaySerializer
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         self.serializer_class = MovieDisplaySerializer
#         return self.create(request, *args, **kwargs)
    

# class MovieDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = MovieSerializer
#         return self.retrieve(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         self.serializer_class = MovieDisplaySerializer
#         return self.partial_update(request, *args, **kwargs)
        
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class UserList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = User.objects.all()

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = UserDisplaySerializer
#         return self.list(request, *args, **kwargs)


# class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = UserSerializer
#         return self.retrieve(request, *args, **kwargs)


class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class MovieDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'users' : reverse('user-list', request=request, format=format),
        'movies' : reverse('movie-list', request=request, format=format)
    })






# Using Generic Class - Based Views

# from apiapp.models import Movie
# from apiapp.serializers import MovieSerializer, UserSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework import permissions


# class MovieList(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)

# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

