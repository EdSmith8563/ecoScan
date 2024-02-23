from django.db import models
from django.contrib.auth.models import User, Group, Permission
from map.models import Location

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.user
    


class UserLocation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    points_obtained = models.IntegerField(default=0)
    questions_answered_right = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'location')

