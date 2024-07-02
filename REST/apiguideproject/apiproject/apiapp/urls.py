from django.urls import path, include
from apiapp import views
from rest_framework.urlpatterns import format_suffix_patterns


# Function - Based View - URLs

# urlpatterns = [
#     path('movies/', views.movie_list),
#     path('movies/<int:pk>/', views.movie_detail),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)




# Class - Based View - URLs

# urlpatterns = [
#     path('movies/', views.MovieList.as_view()),
#     path('movies/<int:pk>/', views.MovieDetail.as_view()),

#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
#     path('', views.api_root)
# ]





# API Endpoints

urlpatterns = format_suffix_patterns([

    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),

    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])