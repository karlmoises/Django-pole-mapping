# resources.py
from import_export import resources
from .models import *

class ElectricPoleResource(resources.ModelResource):
    class Meta:
        model = ElectricPole

class PoleInstallationResource(resources.ModelResource):
    class Meta:
        model = PoleInstallation

class ElectricPoleConnectionResource(resources.ModelResource):
    class Meta:
        model = ElectricPoleConnection