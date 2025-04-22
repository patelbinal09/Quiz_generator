from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-quiz/', views.generate_quiz, name='generate_quiz'),
] 