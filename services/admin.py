from django.contrib import admin
from services.models import Service
from services.models import ServicePersonnel, RangeOfCoverage, ServicePersonnelDemand, WorkSample

# Register your models here.

admin.site.register(Service)
admin.site.register(ServicePersonnel)
admin.site.register(RangeOfCoverage)
admin.site.register(ServicePersonnelDemand)
admin.site.register(WorkSample)
