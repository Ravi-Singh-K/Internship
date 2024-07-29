from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from userapp.serializers import *
from userapp.views import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView





# registration = UserRegistrationViewSet.as_view({
#     'post' : 'create',
#     'get' : 'list'
# })

# faculty_create = FacultyViewSet.as_view({
#     'post' : 'create'

# })
# faculty_list = FacultyViewSet.as_view({
#     'get' : 'list'
# })
# faculty_detail = FacultyViewSet.as_view({
#     'get' : 'retrieve',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })


# group_create = GroupViewSet.as_view({
#     'post' : 'create'
# })
# group_list = GroupViewSet.as_view({
#     'get' : 'list'
# })
# group_detail = GroupViewSet.as_view({
#     'get' : 'retrieve',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

# book_create = BookViewSet.as_view({
#     'post' : 'create'
# })
# book_list = BookViewSet.as_view({
#     'get' : 'list'
# })
# book_detail = BookViewSet.as_view({
#     'get' : 'retrieve',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

# @api_view(['get'])
# def api_root(request, format = None):
#     return Response({
#        'User Login' : reverse('jwt-login', request=request, format=format),
#        'Token Refresh' : reverse('token_refresh', request=request, format=format),
#        'Registration' : reverse('registration-list', request=request, format=format),
#        'Faculty' : reverse('faculty-list', request=request, format=format),
#        'Group' : reverse('group-list', request=request, format=format),
#        'Book' : reverse('book-list', request=request, format=format),
       
#     #    'View Faculty' : reverse('list-faculty', request=request, format=format),
#     #    'Create Faculty' : reverse('create-faculty', request=request, format=format),
#     #    'View Group' : reverse('list-group', request=request, format=format),
#     #    'Create Group' : reverse('create-group', request=request, format=format),
#     #     'Create Book' : reverse('create-book', request=request, format=format),
#     #     'View Book' : reverse('list-book', request=request, format=format),
#     })

# router = routers.SimpleRouter()
# router.register(r'registration', UserRegistrationViewSet, basename='registration')
# router.register(r'faculties', FacultyViewSet, basename='faculty')
# router.register(r'groups', GroupViewSet, basename='group')
# router.register(r'books', BookViewSet, basename='book')
# urlpatterns = rJWTLoginViewouter.urls

# urlpatterns = [
#     path('', api_root),
#     path('api-auth/', include('rest_framework.urls')),
#     # path('registration/', registration, name = 'registration'),
#     path('api/login/', .as_view(), name='jwt-login'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # path('create-faculty/', faculty_create, name = 'create-faculty'),
#     # path('list-faculty/', faculty_list, name='list-faculty'),
#     # path('list-faculty/<int:pk>/', faculty_detail, name='update-faculty'),

#     # path('create-group/', group_create, name = 'create-group'),
#     # path('list-group/', group_list, name='list-group'),
#     # path('list-group/<int:pk>/', group_detail, name='update-group'),

#     # path('create-book/', book_create, name = 'create-book'),
#     # path('list-book/', book_list, name='list-book'),
#     # path('list-book/<int:pk>/', book_detail, name='update-book'),
# ]

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'User Login': reverse('jwt-login', request=request, format=format),
#         'Token Refresh': reverse('token_refresh', request=request, format=format),
#         'Registration': reverse('registration-list', request=request, format=format),
#         'Faculty': reverse('faculty-list', request=request, format=format),
#         'Group': reverse('group-list', request=request, format=format),
#         'Book': reverse('book-list', request=request, format=format),
#         # 'Assign Book' : reverse('assign-list', request=request, format=format),
#         # 'Transfer Book' : reverse('transfer-list', request=request, format=format),
#     })


# router.register(r'assignbook', AssignBookViewSet, basename='assign')
# router.register(r'transfer', BookTransferViewSet, basename='transfer')


# urlpatterns = router.urls + [
#     # path('', api_root, name='api-root'),
#     path('api-auth/', include('rest_framework.urls')),
#     # path('api/login/', JWTLoginView.as_view(), name='jwt-login'),
#     # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]













router = routers.DefaultRouter()
router.register(r'registration', UserRegistrationViewSet, basename='registration')
router.register(r'faculties', FacultyViewSet, basename='faculty')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'books', AllBookViewSet, basename='book')
router.register(r'assignbooks', BookAssignmentViewSet, basename='assignbook')
router.register(r'requestbooks', RequestBookViewSet, basename='requestbook')

urlpatterns = router.urls + [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)