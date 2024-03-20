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
        user_profile = request.user.profile

        # Query the database for locations associated with the user where questions were answered correctly
        completed_locations_query = UserLocation.objects.filter(
            user=user_profile,
            questions_answered_right__gt=0
        ).select_related('location').values('location__name', 'points_obtained')

        completed_locations = [
            {'name': loc['location__name'], 'points': loc['points_obtained']} 
            for loc in completed_locations_query
        ]
        
        # Add the total points to the context
        context = {
            'completed_locations': completed_locations,
            'total_points': user_profile.total_points,  
        }
        
    except UserProfile.DoesNotExist:
        return redirect('login') # If the UserProfile is not found, redirect the user to the login page

    return render(request, 'map.html', context)