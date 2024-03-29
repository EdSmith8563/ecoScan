from django.contrib import admin
from django.urls import path, include
from map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map_view, name='map'),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('camera/', include('camera.urls')),
    path('about/', include('about.urls')),
]
    