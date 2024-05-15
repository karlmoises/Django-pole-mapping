from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from import_export.admin import ImportExportModelAdmin
from .models import ElectricPole, ElectricPoleConnection
from .forms import ElectricPoleConnectionForm
from .resources import *


class PoleInstallationInline(admin.TabularInline):
    model = PoleInstallation
    extra = 1

class ElectricPoleAdmin(ImportExportModelAdmin):
    resource_class = ElectricPoleResource
    list_display = ['pole_ID', 'latitude', 'longitude']
    search_fields = ['pole_ID']
    inlines = [PoleInstallationInline]      

admin.site.register(ElectricPole, ElectricPoleAdmin)

class ElectricPoleConnectionAdmin(ImportExportModelAdmin):
    list_display = ['pole_from', 'pole_to']
    search_fields = ['pole_from__pole_ID', 'pole_to__pole_ID']

admin.site.register(ElectricPoleConnection, ElectricPoleConnectionAdmin)

admin.site.register(PoleInstallation)