from .models import *
import django_filters as filters

class LandFilter(filters.FilterSet):
    class Meta:
        model = LandPost
        fields = ['state']