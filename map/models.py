from django.db import models

# Create your models here.
class Location(models.Model):
    location_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
