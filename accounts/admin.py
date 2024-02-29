from django.contrib import admin
from .models import *

admin.site.register(UserAchievement)

# Custom admin class for the UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'display_level')

    def display_level(self, obj):
        return obj.level()
    display_level.short_description = 'Level'

admin.site.register(UserProfile, UserProfileAdmin)

# Custom admin class for the UserLocation model
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'points_obtained', 'questions_answered_right')

admin.site.register(UserLocation, UserLocationAdmin)