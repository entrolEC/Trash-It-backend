from django.shortcuts import render
from rest_framework import viewsets
from location.serializers import TrashcanSerializer
from location.models import Trashcan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from location.permissions import *

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
    #http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly]