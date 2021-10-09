from rest_framework import serializers
from .models import CustomUser
from location.models import Trashcan

class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Trashcan.objects.all())
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'spouse_name', 'date_of_birth', 'author']
        
