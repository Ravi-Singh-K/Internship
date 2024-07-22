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
# from rest_framework_nested import routers
from rest_framework import routers
from .views import UserViewSet, MovieViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)

# users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
# users_router.register(r'movies', MovieViewSet, basename='user-movies')

urlpatterns = format_suffix_patterns([

    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # path('', include(users_router.urls)),
])