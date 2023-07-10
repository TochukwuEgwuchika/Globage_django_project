from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import ProfileForm
from accommodation.models import AccommodationPost
from land.models import LandPost
from building.models import BuildingPost
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    accommodations = AccommodationPost.objects.all()
    return render(request, 'accounts/home.html', {'accommodations':accommodations})
    
def about(request):
    return render(request, 'accounts/about.html')
    


def sign_up(request):
    form = RegisterForm()
    profile_form = ProfileForm()

    if request.user.is_authenticated:
        return redirect('/dashboard')        
    if request.method == 'POST':
        form = RegisterForm(request.POST)        
        if form.is_valid():
            user = form.save()    
            login(request, user)        
            profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
            print(profile_form)
            if profile_form.is_valid():
                profile_form.save()                
                return redirect('/dashboard')

        else:
            messages.error(request, ('Please correct the error below.'))


    else:
        form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, 'registration/sign_up.html', {'form':form, 'profile_form':profile_form})



   



    

def dashboard(request):
    if request.user.is_authenticated:
        accommodation_num = AccommodationPost.objects.filter(author=request.user).count()
        building_num = BuildingPost.objects.filter(author = request.user).count()
        land_num = LandPost.objects.filter(author = request.user).count()
        return render(request, 'accounts/dashboard.html', {'accommodation_num': accommodation_num, 'building_num':building_num, 'land_num': land_num})
    else:
        return redirect('/login')

