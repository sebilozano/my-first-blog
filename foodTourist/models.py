from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from django.http import QueryDict

# Create your models here.


class Itinerary(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class ItineraryStop(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.PROTECT)
    stop = models.CharField(max_length=100)

class ItineraryForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")

    def __init__(self, *args, **kwargs):
        if args:
            print(args[0])
            args = QueryDict(args[0])
            print(args)
            super().__init__(args, **kwargs)
            print("KEYSSSSS")
            for key in args:
                print(key)

            stops = ItineraryStop.objects.filter(
                itinerary=self.instance
            )

            for key in args:
                if key.startswith("stop_"):
                    self.fields[key] = forms.CharField(required=False)
                try:
                    self.initial[key] = args[key][0]
                except IndexError:
                    self.initial[key] = ""

        else:
            super().__init__(*args, **kwargs)
            stops = ItineraryStop.objects.filter(
                itinerary=self.instance
            )

            for i in range(len(stops) + 1):
                field_name = 'stop_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = stops[i].stop
            except IndexError:
                self.initial[field_name] = ""

            #create an extra blank field
            field_name = 'stop_%s' % (i, )
            self.fields[field_name] = forms.CharField(required=False)

    def clean(self):
        stops = set()
        i = 0
        field_name = 'stop_%s' % (i,)

        while self.cleaned_data.get(field_name):
            stop = self.cleaned_data[field_name]
            if stop in stops:
                self.add_error(field_name, 'Duplicate')
            elif stop.strip() == "":
                continue
            else:
                stops.add(stop)
            i += 1
            field_name = 'stop_%s' % (i,)
        self.cleaned_data["stops"] = stops


    def save(self):
        itinerary = self.instance
        itinerary.first_name = self.cleaned_data["first_name"]
        itinerary.last_name = self.cleaned_data["last_name"]
        itinerary.save()

        itinerary.itinerarystop_set.all().delete()
        print(self.cleaned_data)
        print("ETWEEN")
        print(self.cleaned_data["stops"])
        for stop in self.cleaned_data["stops"]:
            ItineraryStop.objects.create(
                itinerary=itinerary,
                stop=stop,
            )

    def get_other_fields(self):
        for field_name in self.fields:
            if not field_name.startswith("stop_"):
                yield field_name

    def get_stop_fields(self):
        for field_name in self.fields:
            if field_name.startswith("stop_"):
                yield self[field_name]


    class Meta:
        model = Itinerary
        fields = '__all__'
