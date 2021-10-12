from rest_framework.permissions import BasePermission
from location.models import Trashcan
from django.contrib.auth.models import User

SAFE_METHODS = ['GET']

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        #print(request.auth)
        print(request.user)
        #print(view.kwargs)
        print(request.method)
        print("IsAuthenticatedOrReadOnly")
        try:
            post = Trashcan.objects.get(pk=view.kwargs['pk'])
            print(post)
        except:
            if request.user.is_superuser:
                print(11)
                return True
            elif (request.method in SAFE_METHODS):
                print(12)
                return True
            elif (request.user and not request.user.is_anonymous and request.method == 'POST'):
                print(13)
                return True
            else:
                print(14)
                return False
        if request.user.is_superuser:
            print(1)
            return True
        elif (request.method in SAFE_METHODS):
            print(2)
            return True
        elif (request.method == 'DELETE' and request.user.email == post.author.email):
            print(3)
            return True
        else:
            print(4)
            return False
