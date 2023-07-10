from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from services.models import ServicePersonnelForm
from services.models import ServicePersonnel, ServicePersonnelDemand, WorkSample, Service
from verification.models import UserVerification
from django.contrib.auth.decorators import login_required
from .filters import ServicePersonnelFilter
from django.core.paginator import Paginator
# Create your views here.

@login_required
def become_service_personnel(request):
    user = request.user
    if user.userverification.verification_status == 'Verified' and user.userverification.is_payment_up_to_date:
        if request.method == 'POST':
            form = ServicePersonnelForm(request.POST)
            images = request.FILES.getlist('images')
            for image in images:
                WorkSample.objects.create(image=image, posted_by = request.user)
            personnel = form.save(commit = False)
            personnel.service_personnel = request.user
            personnel.save()
            user.profile.is_service_personnel_registered = True
            user.profile.save()

            return redirect('/dashboard')

        form = ServicePersonnelForm()
        return render(request, 'services/become_service_personnel.html', {'form': form })

    elif user.userverification.verification_status == 'Pending':
        return render(request, 'verification/verification_pending.html')
        
    elif user.userverification.verification_status == 'Verified' and not user.userverification.is_payment_up_to_date:
        return render(request, 'verification/subscription_expired.html')
        
    else:
        return redirect('/verification/get_verified')



def hire_services(request):
    service_personnels = ServicePersonnel.objects.order_by('date_became_service_personnel')  
    #service_personnel_filter = ServicePersonnelFilter(request.GET, queryset=service_personnels)       
    #service_personnels = service_personnel_filter.qs
    
    service = request.GET.get('service', None)
    location = request.GET.get('location', None)
    if service is not None:
        service_personnels = ServicePersonnel.objects.filter(service_provided = service)
        if location is not None:
            service_personnels = service_personnels.filter(location__icontains = location)
            
        
    

    p = Paginator(service_personnels, 20)
    page = request.GET.get('page')
    services_list = p.get_page(page)
    services = Service.objects.all()

    return render(request, 'services/hire.html', {'service_personnels': service_personnels, 'services_list':services_list, 'services': services})


def hire(request, id):
    service_personnel = ServicePersonnel.objects.get(id = id )
    phone = service_personnel.service_personnel.profile.phone_number
    phone = '234'+ str(int(phone))
    message = f"I%20need%20your%20service%20as%20a%20{service_personnel.service_provided}%20.%20_From Globage_"
    print("Parameters obtained")
    a = ServicePersonnelDemand.objects.all().first()
    a.demand+=1
    a.save()
    print(ServicePersonnelDemand.objects.all().first().demand)
    return redirect(f'https://wa.me/{phone}?text={message}')
    
def view_work_samples(request, id):
    id+=1
    user = User.objects.get(id = id )
    work_samples = WorkSample.objects.filter(posted_by = user)
    return render(request, 'services/work_samples.html', {'work_samples': work_samples})
