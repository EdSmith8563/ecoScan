from django.db import models
from django.contrib.auth.models import User
from map.models import Location
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Defines a UserProfile model that extends models.Model
class UserProfile(models.Model):
    THEME_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
    )
    theme_preference = models.CharField(max_length=5, choices=THEME_CHOICES, default='dark')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    total_points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Check if this is a new record or if the total_points was updated to 600
        if self._state.adding or (self.pk and 600 == self.total_points and UserProfile.objects.get(pk=self.pk).total_points != 600):
            self.send_congratulatory_email()
        super(UserProfile, self).save(*args, **kwargs)
        
    # Sends a congratulatory email to the user when they reach 600 points
    def send_congratulatory_email(self):
        subject = 'Congratulations on reaching 600 points!'
        message = 'Dear {},\n\nYour sustainability knowledge has truly paid off!\n\nThis email certifies you as an ecoScan Hero!\nYou have successfully discovered all sustainable locations around Streatham Campus, answering all questions correctly.\n\nKeep up the great work!\n\nRegards,\nThe EcoScan Team.'.format(self.user.username)
        from_email = 'ecoscan-exeter@outlook.com' 
        recipient_list = [self.user.email]
        
        send_mail(subject, message, from_email, recipient_list)
    
    # Returns the user's level based on their total points
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
        
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",  
        related_query_name="customuser", 
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions", 
        related_query_name="customuser",  
    )

# Signal receiver to update total_points on UserLocation save
@receiver(post_save, sender=UserLocation)
def update_user_points_on_save(sender, instance, **kwargs):
    user_profile = instance.user
    total_points = UserLocation.objects.filter(user=user_profile).aggregate(models.Sum('points_obtained'))['points_obtained__sum'] or 0
    UserProfile.objects.filter(pk=user_profile.pk).update(total_points=total_points)

# Signal receiver to update total_points on UserLocation delete
@receiver(post_delete, sender=UserLocation)
def update_user_points_on_delete(sender, instance, **kwargs):
    user_profile = instance.user
    total_points = UserLocation.objects.filter(user=user_profile).aggregate(models.Sum('points_obtained'))['points_obtained__sum'] or 0
    UserProfile.objects.filter(pk=user_profile.pk).update(total_points=total_points)