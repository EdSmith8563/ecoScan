from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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
from django.db.models import Count
from .forms import AddEmailForm


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
        user_quizzes = UserLocation.objects.filter(user=user_profile).order_by('-points_obtained')
        leaderboard = UserProfile.objects.annotate(total_locations_discovered=Count('userlocation__location', distinct=True)).order_by('-total_points')

        context = {
            'user_quizzes': user_quizzes,
            'leaderboard': leaderboard,
        }
    return render(request, 'base.html', context)

# Checks if username already exists in database
class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('A user with that username already exists.')
        return username
    
# Handles user registration using custom form
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
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

# Retrieves and returns JSON data of locations associated with a specific user
@login_required
def get_user_locations(request, user_id):
    try:
        user_profile = UserProfile.objects.get(user__id=user_id)
        locations = UserLocation.objects.filter(user=user_profile).values('location__name', 'questions_answered_right', 'points_obtained')
        data = list(locations)
        return JsonResponse(data, safe=False)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
# Allows authenticated users to add or update their email address through a form
@login_required
def add_email_view(request):
    if request.method == 'POST':
        form = AddEmailForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'Email added successfully!')
            return redirect('home')
    else:
        form = AddEmailForm()
    return render(request, 'add_email.html', {'form': form})