from rest_framework.permissions import BasePermission
from userapp.models import *

class NotAuthenticated(BasePermission):
    """
        Custom permission to allow only unauthenticated users to perform certain actions.

        This permission is used to ensure that only users who are not logged in can register a new users. It is useful for views that handles user registration.

        Methods :
            has_permission(request, view) : Checks if user is not authenticated

        Parameters :
            request(HttpRequest) : The request object.
            view(APIView) : The view object.
        
        Returns :
            boolean :
                - True if the user is not authenticated or is staff.
                - False if the user is authenticated and not staff.
    """

    def has_permission(self, request, view):
        """
            Determine if the request should be permitted.
            
            Parameters :
                request (HttpRequest) : The request object.
                view (APIView) : The view object.
            
            Returns :
                bool :
                    - True if the user is not authenticated or is staff.
                    - False if the user is authenticated and not staff.
        """
        if request.user and request.user.is_authenticated and not request.user.is_staff:
            return False
        else:
            return True

class IsLibrarian(BasePermission):
    """
        Custom permission to only allow users in the 'librarian' group to perform CRUD operations on books.

        Methods:
            has_permission(request, view): Checks if the user is in the 'librarian' group.

        Parameters :
            request (HttpRequest) : The request object.
            view (APIView) : The view object.
        
        Returns :
            bool :
                - True if user is in librarian group
                - False if user is not in librarian group.
    """

    def has_permission(self, request, view):
        """
            Determine if the request should be permitted.

            Parameters :
                request (HttpRequest) : The request object.
                view (APIView) : The view object.
        
            Returns:
                bool: True if the user is in the 'librarian' group, False otherwise.
        """

        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if request.user.primary_group and request.user.primary_group.name == 'Librarian':
                return True
        return False