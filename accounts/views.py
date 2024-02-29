from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count
from .models import UserProfile, UserLocation

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# A view function that renders the GDPR information page
def gdpr_sigup_view(request):
    return render(request, 'registration/GDPR.html')

# A view function that renders the terms and conditions page
def term_sigup_view(request):
    return render(request, 'registration/termsandconditions.html')

# A view function for the homepage
def home(request):
    context = {}
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        user_quizzes = UserLocation.objects.filter(user=user_profile)
        leaderboard = UserProfile.objects.annotate(total_locations_discovered=Count('userlocation__location', distinct=True)).order_by('-total_points')[:10]

        context = {
            'user_quizzes': user_quizzes,
            'leaderboard': leaderboard,
        }
    return render(request, 'base.html', context)