# In models.py

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ElectricPole(models.Model):
    pole_ID = models.CharField(max_length=100)
    location = gis_models.PointField(null=True, blank=True)

    def __str__(self):
        return self.pole_ID

class PoleInstallation(models.Model):
    pole = models.ForeignKey(ElectricPole, related_name='installations', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, related_name='installations', on_delete=models.CASCADE, default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.device.name} on {self.pole.pole_ID}"

class ElectricPoleConnection(models.Model):
    pole_from = models.ForeignKey(ElectricPole, related_name='connections_from', on_delete=models.CASCADE)
    pole_to = models.ForeignKey(ElectricPole, related_name='connections_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pole_from.pole_ID} to {self.pole_to.pole_ID}'