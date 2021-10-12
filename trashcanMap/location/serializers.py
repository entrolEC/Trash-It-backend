from location.models import Trashcan
from rest_framework import serializers
from accounts.serializers import UserSerializer

class PinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Trashcan
        fields = ('id', 'latitude', 'longitude')

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'author')


