from django.db import models
from django.contrib.auth.models import User, Group, Permission
from map.models import Location

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
    
    def level(self):
        if self.total_points < 25:
            return 0  # Consider level 0 for less than 25 points
        elif self.total_points < 50:
            return 1
        elif self.total_points < 75:
            return 2
        elif self.total_points < 100:
            return 3
        elif self.total_points < 150:
            return 4  # Consider level 0 for less than 25 points
        elif self.total_points < 200:
            return 5
        elif self.total_points < 250:
            return 6
        elif self.total_points < 300:
            return 7
        elif self.total_points < 350:
            return 8  # Consider level 0 for less than 25 points
        elif self.total_points < 400:
            return 9
        elif self.total_points < 450:
            return 10
        elif self.total_points < 500:
            return 11
        
        # Add more levels as needed
        else:
            return 4  # Consider this for 100 or more points


class UserLocation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    points_obtained = models.IntegerField(default=0)
    questions_answered_right = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'location')
    def __str__(self):
        return self.location.name
        


class UserAchievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(UserProfile, related_name='achievements')

    def __str__(self):
        return self.name