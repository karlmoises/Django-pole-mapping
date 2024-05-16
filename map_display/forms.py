# In forms.py
from django import forms
from dal import autocomplete
from django.contrib.gis import forms
from .models import *
from django.contrib.gis import forms as gis_forms
from django.contrib.gis.db.models.functions import AsGeoJSON
from leaflet.forms.widgets import LeafletWidget



class ElectricPoleForm(forms.ModelForm):
    class Meta:
        model = ElectricPole
        fields = '__all__'
        # widgets = {
        #     'location': forms.OSMWidget(attrs={'map_width': 800, 'map_height': 600}),
        # }



class ElectricPoleConnectionForm(forms.ModelForm):
    class Meta:
        model = ElectricPoleConnection
        fields = ['pole_from', 'pole_to']

class ElectricPoleAdminForm(forms.ModelForm):
    class Meta:
        model = ElectricPole
        fields = '__all__'