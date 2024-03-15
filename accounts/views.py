from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count
from .models import UserProfile, UserLocation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages 
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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
        leaderboard = UserProfile.objects.annotate(total_locations_discovered=Count('userlocation__location', distinct=True)).order_by('-total_points')

        context = {
            'user_quizzes': user_quizzes,
            'leaderboard': leaderboard,
        }
    return render(request, 'base.html', context)

class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('A user with that username already exists.')
        return username
    
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"
    def form_valid(self, form):
        response = super().form_valid(form)
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # super().form_valid(form)  # This saves the user to the database
        user = form.instance
        # Log the user in
        login(self.request, user)
        messages.success(self.request, f'Congratulations {user.username}, your account has been created!')
        return response
@login_required
@require_POST
def update_theme_preference(request):
    # Get the new theme preference from the request
    new_theme = request.POST.get('theme_preference')
    
    # Update the user's UserProfile
    profile = request.user.profile
    profile.theme_preference = new_theme
    profile.save()
    
    return JsonResponse({'status': 'success'})