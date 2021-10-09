from location.models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    #name = serializers.ReadOnlyField(source='name.username')

    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'name', 'author')


