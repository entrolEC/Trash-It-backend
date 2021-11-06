from rest_framework import serializers
from django.core import serializers as sl
from .models import CustomUser
from location.models import Trashcan
import json
from datetime import date, timedelta

class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Trashcan.objects.all())
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username','date_of_birth', 'author']
        
class UserDetailSerializer(serializers.ModelSerializer):
    log = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    def get_log(self, obj):
        today = date.today() + timedelta(days=1)
        endday = today - timedelta(days=7)
        queryset = Trashcan.objects.filter(author=self.context.get("user_id"))
        timeQuerySet = queryset.filter(timestamp__range=[endday, today])
        listQuerySet = list(timeQuerySet)
        resData = {}
        jsonData = json.loads(sl.serialize('json', listQuerySet))

        for item in jsonData:
            item['fields']['pk'] = item['pk']
            if str(item['fields']['timestamp'][5:10]) in resData:
                resData[str(item['fields']['timestamp'][5:10])].append(item['fields'])
            else:
                resData[str(item['fields']['timestamp'][5:10])] = []
                resData[str(item['fields']['timestamp'][5:10])].append(item['fields'])
        return resData
    
    def get_total(self, obj):
        return Trashcan.objects.filter(author=self.context.get("user_id")).count()

    def get_id(self, obj):
        return obj.first().id

    def get_email(self, obj):
        return obj.first().email

    def get_username(self, obj):
        return obj.first().username
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'log', 'total']