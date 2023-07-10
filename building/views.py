from django.shortcuts import render,redirect
from building.models import BuildingPostForm, BuildingPost, BuildingDemand,BuildingType
from django.contrib.auth.decorators import login_required
from .filters import BuildingFilter
from django.core.paginator import Paginator

# Create your views here.

def view_building(request):
    buildings = BuildingPost.objects.all()
    categories = BuildingType.objects.all()
    #building_filter = BuildingFilter(request.GET, queryset=buildings)
    #buildings = building_filter.qs
    
    
    if request.method == 'GET':
        category = request.GET.get('category', None)
        location = request.GET.get('location', None)
        
        if location is not None:
            if category is not None:
                category = int(category)
                #category = BuildingType.objects.get(id = category).type
            location = str(location).split()
            #if category is not None:
                #location.append(str(category))
            for loc in location:
                if loc == 'in' or loc == 'at' or loc == 'by' or loc == 'state':
                    continue
                buildings1 = BuildingPost.objects.filter(location__icontains = str(loc)).filter(category = category)
                buildings2 =  BuildingPost.objects.filter(lga__icontains = str(loc)).filter(category=category)
                '''buildings3 =  BuildingPost.objects.filter(category__type__icontains = str(loc)).filter(category = category)'''
                buildings4 =  BuildingPost.objects.filter(state__state_name__icontains = str(loc)).filter(category = category)
                buildings = buildings1 | buildings2 | buildings4
                

            buildings = buildings.order_by('-date_posted')

    p = Paginator(buildings, 20)
    page = request.GET.get('page')
    buildings_list = p.get_page(page)
    

    return render(request, 'building/building.html', {'buildings': buildings, 'buildings_list':buildings_list, 'categories': categories})

    

@login_required
def post_building(request):
    user = request.user
    if user.userverification.verification_status == 'Verified':
        if request.method == 'POST':
            form = BuildingPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.author = request.user
                post.save()
                return redirect('/dashboard')
        else:
            form = BuildingPostForm()
            return render(request, 'building/post_building.html', {'form':form})
    elif user.userverification.verification_status == 'Pending':
        return render(request, 'verification/verification_pending.html')
    else:
        return redirect('/verification/get_verified')


@login_required
def manage_building_posts(request):
    my_building_posts = BuildingPost.objects.filter(author = request.user)
    return render(request, 'building/manage_building_posts.html', {'my_building_posts':my_building_posts})


@login_required
def delete_building_post(request, post_id):
    post = BuildingPost.objects.get(id = post_id)
    post.delete()
    return redirect('/building/my-posts')


def secure_building(request, post_id):
    building = BuildingPost.objects.get(id = post_id )
    phone = building.author.profile.phone_number
    phone = '234'+ str(int(phone))
    message = f"I'm%20interested%20in%20buying%20the%20building:%20{building.category}%20at%20{building.location}%20in%20{building.lga}"
    print("Parameters obtained")
    a = BuildingDemand.objects.all().first()
    a.demand+=1
    a.save()
    print(BuildingDemand.objects.all().first().demand)
    return redirect(f'https://wa.me/{phone}?text={message}')



    