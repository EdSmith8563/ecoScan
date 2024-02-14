from django.shortcuts import render
def map_view(request):
    context = {
        'latitude': 'Exeter University latitude',
        'longitude': 'Exeter University longitude',
        # Pass other context data as needed
    }
    return render(request, 'map.html', context)
# Create your views here.
