from django.shortcuts import render
from rest_framework import viewsets
from location.serializers import TrashcanSerializer
from location.models import Trashcan, Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from location.permissions import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
    #http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly]

class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        profile = Profile(user=user, nickname=request.data['nickname'])

        user.save()
        profile.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})