from django.db import models

class Trashcan(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to="location/media/image")