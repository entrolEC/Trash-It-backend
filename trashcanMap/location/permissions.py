from rest_framework.permissions import BasePermission
from location.models import Trashcan

SAFE_METHODS = ['POST','GET', 'HEAD', 'OPTIONS']

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        print(request.auth)
        print(view.kwargs)
        if not request.auth:
            return False
        try:
            post = Trashcan.objects.get(pk=view.kwargs['pk'])
        except:
            if request.user.is_superuser:
                return True
            elif (request.user and request.method in SAFE_METHODS):
                return True
            else:
                return False
        if request.user.is_superuser:
            return True
        elif (request.user and request.method in SAFE_METHODS):
            return True
        elif (request.mathod == 'DELETE' and request.user == post.user):
            return True
        else:
            return False