from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .forms import *
from .resources import *


class PoleInstallationInline(admin.TabularInline):
    model = PoleInstallation
    extra = 1

class ElectricPoleAdminForm(forms.ModelForm):
    class Meta:
        model = ElectricPole
        fields = '__all__'

    latitude = forms.FloatField(label='Latitude', required=False)
    longitude = forms.FloatField(label='Longitude', required=False)

class ElectricPoleAdmin(ImportExportModelAdmin, LeafletGeoAdmin):
    resource_class = ElectricPoleResource
    list_display = ['pole_ID', 'location',]
    search_fields = ['pole_ID']
    inlines = [PoleInstallationInline]
    form = ElectricPoleAdminForm  

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['latitude'].initial = obj.location.y
            form.base_fields['longitude'].initial = obj.location.x
        return form
    
    def save_model(self, request, obj, form, change):
        latitude = form.cleaned_data.get('latitude')
        longitude = form.cleaned_data.get('longitude')
        if latitude is not None and longitude is not None:
            obj.location = Point(longitude, latitude)
        super().save_model(request, obj, form, change)

admin.site.register(ElectricPole, ElectricPoleAdmin)

class ElectricPoleConnectionAdmin(ImportExportModelAdmin):
    list_display = ['pole_from', 'pole_to']
    search_fields = ['pole_from__pole_ID', 'pole_to__pole_ID']

admin.site.register(ElectricPoleConnection, ElectricPoleConnectionAdmin)

admin.site.register(PoleInstallation)