from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserLocation)
admin.site.register(UserAchievement)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'display_level')

    def display_level(self, obj):
        return obj.level()
    display_level.short_description = 'Level'

admin.site.register(UserProfile, UserProfileAdmin)