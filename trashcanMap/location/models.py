from django.db import models
from uuid import uuid4
from django.utils import timezone
import os

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

class Trashcan(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=50)
    image = models.FileField(upload_to=date_upload_to, max_length=300)