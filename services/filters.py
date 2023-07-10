from .models import *
import django_filters


class ServicePersonnelFilter(django_filters.FilterSet):
    class Meta:
        model = ServicePersonnel
        fields = [
            'service_provided', 
            'range_of_coverage']
