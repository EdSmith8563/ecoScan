from django.contrib import admin
from django.urls import path, include
from map import views
from accounts import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map_view, name='map'),
    path("accounts/", include("accounts.urls")),
    path('camera/', include('camera.urls')),
]