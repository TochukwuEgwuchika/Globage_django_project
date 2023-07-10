from django.shortcuts import render
from .models import Passphrase
from accommodation.models import AccommodationPost, AccommodationDemand
from building.models import BuildingPost, BuildingDemand
from land.models import LandPost, LandDemand
from services.models import ServicePersonnel, ServicePersonnelDemand

# Create your views here.

def status(request):
    if request.method == 'POST':
        #return render(request, 'status/status.html')
        passphrase = request.POST['passphrase']
        print(passphrase)
        print(Passphrase.objects.all().first().passphrase)
       
        if passphrase == Passphrase.objects.all().first().passphrase:
            num_accommodation = AccommodationPost.objects.count()
            num_building = BuildingPost.objects.count()
            num_land = LandPost.objects.count()
            num_service_personnel = ServicePersonnel.objects.count()

            demand_accommodation = AccommodationDemand.objects.all().first().demand
            demand_building = BuildingDemand.objects.all().first().demand
            demand_land = LandDemand.objects.all().first().demand
            demand_service_personnel = ServicePersonnelDemand.objects.all().first().demand
        
            return render(request, 'status/status.html',
            {
               'num_accommodation':num_accommodation,
               'num_building':num_building,
               'num_land':num_land,
               'num_service_personnel': num_service_personnel,
               'demand_accommodation' : demand_accommodation, 
               'demand_building' : demand_building,
               'demand_land': demand_land,
               'demand_service_personnel': demand_service_personnel

            })
    return render(request, 'status/auth.html')

