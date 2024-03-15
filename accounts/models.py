from django.db import models
from django.contrib.auth.models import User
from map.models import Location

# Defines a UserProfile model that extends models.Model
class UserProfile(models.Model):
    THEME_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
    )
    theme_preference = models.CharField(max_length=5, choices=THEME_CHOICES, default='dark')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    total_points = models.IntegerField(default=0)
    
    # Calculates the user's level based on their total points
    def level(self):
        levels = [25, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800]
        for i, threshold in enumerate(levels, 1):
            if self.total_points < threshold:
                return i
        return len(levels) + 1
    
    # Determines the rank image based on the user's level
    def rank_image(self):
        level = self.level()
        return f'rank_{level}.png' if level <= 12 else 'rank_12.png'
    def __str__(self):
        return self.user.username

# Defines a UserLocation model to store locations associated with a user
class UserLocation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    points_obtained = models.IntegerField(default=0)
    questions_answered_right = models.IntegerField(default=0)

    def __str__(self):
        username = self.user.user.username
        location_name = self.location.name
        return f"{username} - {location_name}"
        
# Defines a UserAchievement model to store achievements that can be earned by users
class UserAchievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(UserProfile, related_name='achievements')

    def __str__(self):
        return self.name