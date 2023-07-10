from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accommodation.models import AccommodationPostForm, AccommodationPost, AccommodationDemand, AccommodationType
from .filters import AccommodationFilter

#Import Pagination Stuff
from django.core.paginator import Paginator


# Create your views here.


def find_accommodation(request):
    
    #accommodations = AccommodationPost.objects.all().order_by('?)
   
    accommodations = AccommodationPost.objects.order_by('-date_posted')
    #accommodation_filter = AccommodationFilter(request.GET, queryset = accommodations)
    #accommodations = accommodation_filter.qs
    
    if request.method == 'GET':
        category = request.GET.get('category', None)
        location = request.GET.get('location', None)
        
        if location is not None:
            if category is not None:
                category = int(category)
                #category = AccommodationType.objects.get(id = category).type
            location = str(location).split()
            #if category is not None:
                #location.append(str(category))
            for loc in location:
                if loc == 'in' or loc == 'at' or loc == 'by' or loc == 'state':
                    continue
                accommodations1 = AccommodationPost.objects.filter(location__icontains = str(loc)).filter(category = category)
                accommodations2 =  AccommodationPost.objects.filter(lga__icontains = str(loc)).filter(category=category)
                '''accommodations3 =  AccommodationPost.objects.filter(category__type__icontains = str(loc)).filter(category = category)'''
                accommodations4 =  AccommodationPost.objects.filter(state__state_name__icontains = str(loc)).filter(category = category)
                accommodations = accommodations1 | accommodations2 | accommodations4
                

            accommodations = accommodations.order_by('-date_posted')
    #Set up paginator
    p = Paginator(accommodations, 20)
    page = request.GET.get('page')
    accommodations_list = p.get_page(page)
    categories = AccommodationType.objects.all()
    return render(request, 'accommodation/accommodation.html', {'range': range(1,20), 'accommodations': accommodations, 'accommodations_list':accommodations_list, 'categories': categories})


def post_accommodation(request):
    if request.user.is_authenticated:
        user = request.user
        if user.userverification.verification_status == 'Verified':
            if request.method == 'POST':
                form = AccommodationPostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit = False)
                    post.author = request.user
                    post.save()
                    return redirect('/dashboard')
            else:
                form = AccommodationPostForm()
                return render(request, 'accommodation/post_accommodation.html', {'form':form})
        elif user.userverification.verification_status == 'Pending':
            return render(request, 'verification/verification_pending.html')
            
        elif user.userverification.is_payment_up_to_date == False:
            return render(request, 'verification/subscription_expired.html')
            
        else:
            return redirect('/verification/get_verified')
    else:
        return redirect('/login')
    

@login_required
def manage_accommodation_posts(request):
    my_accommodation_posts = AccommodationPost.objects.filter(author=request.user)
    return render(request, 'accommodation/manage_accommodation_posts.html', {'my_accommodation_posts':my_accommodation_posts})

@login_required
def delete_accommodation_post(request, post_id):
    post = AccommodationPost.objects.get(id = post_id)
    post.delete()
    return redirect('accommodation/my-posts')


def secure_accommodation(request, post_id):
    accommodation = AccommodationPost.objects.get(id = post_id )
    phone = accommodation.author.profile.phone_number
    phone = '234'+ str(int(phone))
    message = f"I'm%20interested%20in%20securing%20the%20accommodation:%20{accommodation.category}%20at%20{accommodation.location}%20in%20{accommodation.lga}"
    print("Parameters obtained")
    a = AccommodationDemand.objects.all().first()
    a.demand+=1
    a.save()
    print(AccommodationDemand.objects.all().first().demand)
    return redirect(f'https://wa.me/{phone}?text={message}')

