# In models.py

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models



class ElectricPole(models.Model):
    pole_ID = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.pole_ID


class PoleInstallation(models.Model):
    pole = models.ForeignKey(ElectricPole, related_name='installations', on_delete=models.CASCADE)
    installation_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.installation_type} on {self.pole.pole_ID}"


class ElectricPoleConnection(models.Model):
    pole_from = models.ForeignKey(ElectricPole, related_name='connections_from', on_delete=models.CASCADE)
    pole_to = models.ForeignKey(ElectricPole, related_name='connections_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pole_from.pole_ID} to {self.pole_to.pole_ID}'


