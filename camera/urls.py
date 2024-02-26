from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera, name='camera'),
    path('quiz1/', views.quiz1, name='quiz1'),
    path('quiz2/', views.quiz2, name='quiz2'),
    path('quiz3/', views.quiz3, name='quiz3'),
    path('quiz4/', views.quiz4, name='quiz4'),
    path('quiz5/', views.quiz5, name='quiz5'),
    path('quiz6/', views.quiz6, name='quiz6'),
    path('quiz7/', views.quiz7, name='quiz7'),
    path('quiz8/', views.quiz8, name='quiz8'),
    path('quiz9/', views.quiz9, name='quiz9'),
    path('quiz10/', views.quiz10, name='quiz10'),
    path('quiz11/', views.quiz11, name='quiz11'),
    path('quiz12/', views.quiz12, name='quiz12'),
]