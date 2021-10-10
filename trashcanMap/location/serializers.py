from location.models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'author')


