import django_filters
from .models import PoleInstallation

class PoleInstallationFilter(django_filters.FilterSet):
    installation_type = django_filters.CharFilter(field_name='installation_type', lookup_expr='icontains')

    class Meta:
        model = PoleInstallation
        fields = ['installation_type']
