from django.urls import path
from . import views

urlpatterns = [
    path('generateTour/', views.generate_tour, name='generate_tour'),
]
