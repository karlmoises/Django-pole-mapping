# admin_forms.py

from django import forms
from django.contrib.gis.forms import PointField
from django.contrib.gis.forms.widgets import OSMWidget  # Correct import
from .models import ElectricPole

class ElectricPoleAdminForm(forms.ModelForm):
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')
    location = PointField(widget=OSMWidget(attrs={'map_width': 800, 'map_height': 500}))  # Updated

    class Meta:
        model = ElectricPole
        fields = ['pole_ID', 'latitude', 'longitude', 'location']
