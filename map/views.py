from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserLocation, UserProfile
def map_view(request):
    context = {
        'latitude': 'Exeter University latitude',
        'longitude': 'Exeter University longitude',
    }
    return render(request, 'map.html', context)

@login_required
def map_view(request):
    try:
        # Access the UserProfile instance directly from the authenticated user
        user_profile = request.user.profile 
        
        completed_locations = UserLocation.objects.filter(user=user_profile, questions_answered_right__gt=0).values_list('location__name', flat=True)
        
        context = {
            'completed_locations': list(completed_locations),
        }
        
    # Handle cases where the UserProfile does not exist for some reason    
    except UserProfile.DoesNotExist:
        return redirect('login')

    return render(request, 'map.html', context)