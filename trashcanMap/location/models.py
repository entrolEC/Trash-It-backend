from django.db import models
from uuid import uuid4
from django.utils import timezone
import os
from accounts.models import CustomUser

def date_upload_to(instance, filename):
  # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
  ymd_path = timezone.now().strftime('%Y/%m/%d') 
  # 길이 32 인 uuid 값
  uuid_name = uuid4().hex
  # 확장자 추출
  extension = '.jpeg'
  # 결합 후 return
  return '/'.join([
    ymd_path,
    uuid_name + extension,
  ])


class Likes(models.Model):
    user = models.ForeignKey("accounts.CustomUser", related_name='likes_user', on_delete=models.CASCADE)
    trashcan = models.ForeignKey("Trashcan", related_name='trashcan_likes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class DisLikes(models.Model):
    user = models.ForeignKey("accounts.CustomUser", related_name='dislikes_user', on_delete=models.CASCADE)
    trashcan = models.ForeignKey("Trashcan", related_name='trashcan_dislikes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Trashcan(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=50)
    image = models.FileField(upload_to=date_upload_to, max_length=300)
    description = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomUser', related_name='author', on_delete=models.CASCADE, db_column="author")
    likes = models.ManyToManyField('accounts.CustomUser', related_name='likes', blank=True, through='Likes')
    dislikes = models.ManyToManyField('accounts.CustomUser', related_name='dislikes', blank=True, through='DisLikes')