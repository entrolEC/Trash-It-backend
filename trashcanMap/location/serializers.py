from location.models import Trashcan
from rest_framework import serializers

class PinSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')

    class Meta:
        model = Trashcan
        fields = ('id', 'latitude', 'longitude', 'name')

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'author')


