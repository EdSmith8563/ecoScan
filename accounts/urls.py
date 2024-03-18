from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/GDPR/', views.gdpr_sigup_view, name='GDPR'),
    path('signup/termsandconditions/', views.term_sigup_view, name='T&C'),
    path('', views.home, name='home'),
    path('update-theme/', views.update_theme_preference, name='update_theme_preference'),
    path('user/<int:user_id>/locations/', views.get_user_locations, name='user_locations'),
    path('get_user_locations/<int:user_id>/', views.get_user_locations, name='get_user_locations'),
    path('add-email/', views.add_email_view, name='add_email')
]