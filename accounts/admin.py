from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserAchievement)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'display_level')

    def display_level(self, obj):
        return obj.level()
    display_level.short_description = 'Level'

admin.site.register(UserProfile, UserProfileAdmin)

class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'points_obtained', 'questions_answered_right')

    # You can also define search_fields, list_filter, etc., for enhanced usability.

admin.site.register(UserLocation, UserLocationAdmin)