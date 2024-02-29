from django.db import models

class Location(models.Model):
    location_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
