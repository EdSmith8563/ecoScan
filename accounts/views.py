from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def gdpr_sigup_view(request):
    return render(request, 'registration/GDPR.html')

def term_sigup_view(request):

    return render(request, 'registration/termsandconditions.html')
