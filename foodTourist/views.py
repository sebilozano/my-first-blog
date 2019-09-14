from django.shortcuts import render, redirect
from .models import ItineraryForm, ItineraryStop

# Create your views here.

def generate_tour(request):
    if request.method == "POST":
        form = ItineraryForm(request.body)
        if form.is_valid():
            form.save()
            return render(request, 'foodTourist/generateTour.html', {'form': form})
    else:
        form = ItineraryForm()
    return render(request, 'foodTourist/generateTour.html', {'form': form})
