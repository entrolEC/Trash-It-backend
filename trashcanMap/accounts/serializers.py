from rest_framework import serializers
from django.core import serializers as sl
from .models import CustomUser
from location.models import Trashcan
import json
from datetime import date, timedelta

class UserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username','date_of_birth']
        
class UserDetailSerializer(serializers.ModelSerializer):
    log = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    def get_log(self, obj):
        today = date.today()
        endday = today - timedelta(days=7)
        queryset = Trashcan.objects.filter(author=self.context.get("user_id"))
        timeQuerySet = queryset.filter(timestamp__range=[endday, today])
        listQuerySet = list(timeQuerySet)
        return json.loads(sl.serialize('json', listQuerySet))

    def get_id(self, obj):
        return obj.first().id

    def get_email(self, obj):
        return obj.first().email

    def get_username(self, obj):
        return obj.first().username
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'log']