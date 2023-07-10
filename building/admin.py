from django.contrib import admin
from .models import BuildingPost, BuildingType, BuildingDemand

# Register your models here.

admin.site.register(BuildingPost)
admin.site.register(BuildingType)
admin.site.register(BuildingDemand)
