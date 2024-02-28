from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserLocation, UserProfile
def map_view(request):
    context = {
        'latitude': 'Exeter University latitude',
        'longitude': 'Exeter University longitude',
        # Pass other context data as needed
    }
    return render(request, 'map.html', context)
# Create your views here.


@login_required
def map_view(request):
    try:
        # Access the UserProfile instance directly from the authenticated user
        user_profile = request.user.profile  # Using the 'related_name' from UserProfile model
        
        # Now, use this UserProfile instance to filter UserLocation objects
        completed_locations = UserLocation.objects.filter(user=user_profile, questions_answered_right__gt=0).values_list('location__name', flat=True)
        
        context = {
            'completed_locations': list(completed_locations),
        }
        
    except UserProfile.DoesNotExist:
        # Handle cases where the UserProfile does not exist for some reason
        # This should ideally never happen for authenticated users if profiles are created on user creation
        return redirect('login')

    return render(request, 'map.html', context)