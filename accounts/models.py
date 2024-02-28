from django.db import models
from django.contrib.auth.models import User, Group, Permission
from map.models import Location

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
    
    def level(self):
        levels = [25, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800]
        for i, threshold in enumerate(levels, 1):
            if self.total_points < threshold:
                return i
        return len(levels) + 1
    
    def rank_image(self):
        level = self.level()
        return f'rank_{level}.png' if level <= 12 else 'rank_12.png'

class UserLocation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    points_obtained = models.IntegerField(default=0)
    questions_answered_right = models.IntegerField(default=0)

    def __str__(self):
        # Access the username through the user profile's user field
        username = self.user.user.username
        # Access the location name directly
        location_name = self.location.name
        # Return the formatted string
        return f"{username} - {location_name}"
        


class UserAchievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(UserProfile, related_name='achievements')

    def __str__(self):
        return self.name