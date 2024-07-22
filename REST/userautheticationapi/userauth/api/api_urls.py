from api import views
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


single_user_display = views.RegistrationViewSet.as_view({
    'get' : 'retrieve',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

register_user = views.RegistrationViewSet.as_view({
    'post' : 'create'
})

display_user = views.UserDetailViewSet.as_view({
    'get' : 'list'
})

login_user = views.LoginViewSet.as_view({
    'post' : 'create'
})

book_display = views.BookViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

single_book_display = views.BookViewSet.as_view({
    'get' : 'retrieve',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})


@api_view(['get'])
def api_root(request, format = None):
    return Response({
        'register users' : reverse('register-user', request=request, format = format),
        'display users' : reverse('display-user', request=request, format=format),
        'display books' : reverse('book-list', request = request, format = format),
        'login user' : reverse('login-user', request=request, format=format)
    })


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('display_user/', display_user, name='display-user'),
    path('user-registration/', register_user, name='register-user'),
    path('login-user/', login_user, name='login-user'),
    path('lists-of-books/', book_display, name='book-list'),
    path('<int:pk>/', single_user_display, name='user_detail'),
    path('lists-of-books/<int:pk>/', single_book_display, name='book-detail'),
])