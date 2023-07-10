import django_filters as filters
from .models import *

class BuildingFilter(filters.FilterSet):
    class Meta:
        model = BuildingPost
        fields = ['category', 'state']
