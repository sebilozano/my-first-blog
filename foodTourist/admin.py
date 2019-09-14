from django.contrib import admin
from .models import Itinerary, ItineraryStop

# Register your models here.

admin.site.register(Itinerary)
admin.site.register(ItineraryStop)
