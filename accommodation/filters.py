from .models import *
import django_filters as filters


class AccommodationFilter(filters.FilterSet):
    class Meta:
        model = AccommodationPost
        fields = ['category']