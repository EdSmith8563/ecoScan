from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, gdpr_sigup_view
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/GDPR/', views.gdpr_sigup_view, name='GDPR'),
    path('signup/termsandconditions/', views.term_sigup_view, name='T&C')
]