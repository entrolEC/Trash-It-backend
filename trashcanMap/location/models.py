from django.db import models

class Trashcan(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=50)
    image = models.FileField(upload_to="location/media/image", max_length=300)