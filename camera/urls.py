from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera, name='camera'),
    path('quiz/', views.quiz1, name='quiz1'),
    path('quiz/', views.quiz2, name='quiz2'),
    path('quiz/', views.quiz3, name='quiz3'),
    path('quiz/', views.quiz4, name='quiz4'),
    path('quiz/', views.quiz5, name='quiz5'),
    path('quiz/', views.quiz6, name='quiz6'),
    path('quiz/', views.quiz7, name='quiz7'),
    path('quiz/', views.quiz8, name='quiz8'),
    path('quiz/', views.quiz9, name='quiz9'),
    path('quiz/', views.quiz10, name='quiz10'),
    path('quiz/', views.quiz11, name='quiz11'),
    path('quiz/', views.quiz12, name='quiz12'),
]