from django.contrib import admin
from .models import AccommodationType, State, AccommodationPost, AccommodationDemand

# Register your models here.

admin.site.register(AccommodationType)
admin.site.register(State)
admin.site.register(AccommodationPost)
admin.site.register(AccommodationDemand)
