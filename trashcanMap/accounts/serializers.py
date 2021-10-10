from rest_framework import serializers
from .models import CustomUser
from location.models import Trashcan

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username','date_of_birth']
        
