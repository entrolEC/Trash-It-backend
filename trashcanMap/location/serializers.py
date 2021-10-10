from location.models import Trashcan
from rest_framework import serializers
from django.contrib.auth.models import User

class PinSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')

    class Meta:
        model = Trashcan
        fields = ('id', 'latitude', 'longitude', 'name')

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')

    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'name')

class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Trashcan.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'author']