from django.shortcuts import render
from rest_framework import viewsets
from location.serializers import TrashcanSerializer
from location.models import Trashcan


class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer