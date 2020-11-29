from django.shortcuts import render
from rest_framework import viewsets
from location.serializers import TrashcanSerializer, UserSerializer
from location.models import Trashcan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from location.permissions import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'])

        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

class SigninView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response({'error': 1})