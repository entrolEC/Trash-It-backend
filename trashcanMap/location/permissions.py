from rest_framework.permissions import BasePermission
from rest_framework.response import Response

SAFE_METHODS = ['POST','GET', 'HEAD', 'OPTIONS']

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        print(request.user.is_superuser)

        if (request.method in SAFE_METHODS or request.user.is_superuser):
            return True
        return False