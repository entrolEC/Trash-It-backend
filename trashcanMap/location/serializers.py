from location.models import Trashcan
from rest_framework import serializers


class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'user')