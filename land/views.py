from django.shortcuts import render,redirect
from land.models import LandPostForm,LandPost, LandDemand
from .filters import LandFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_land(request):
    lands = LandPost.objects.order_by('-date_posted')
    #land_filter = LandFilter(request.GET, queryset = lands)
    #lands = land_filter.qs
    
    if request.method == 'GET':
        location = request.GET.get('location', None)
        if location is not None:
            location = str(location).split()
            #if category is not None:
                #location.append(str(category))
            for loc in location:
                if loc == 'in' or loc == 'at' or loc == 'by' or loc == 'state':
                    continue
                lands1 = LandPost.objects.filter(location__icontains = str(loc))
                lands2 =  LandPost.objects.filter(lga__icontains = str(loc))
                lands4 =  LandPost.objects.filter(state__state_name__icontains = str(loc))
                lands = lands1 | lands2 | lands4
                

            lands = lands.order_by('-date_posted')

    p = Paginator(lands, 20)
    page = request.GET.get('page')
    lands_list = p.get_page(page)

    return render(request, 'land/land.html', {'lands':lands, 'lands_list':lands_list})



def post_land(request):
    if request.user.is_authenticated:
        user = request.user
        if user.userverification.verification_status == 'Verified':
            if request.method == 'POST':
                form = LandPostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit = False)
                    post.author = request.user
                    post.save()
                    return redirect('/dashboard')

            form = LandPostForm()
            return render(request, 'land/post_land.html', {'form':form})

        elif user.userverification.verification_status == 'Pending':
            return render(request, 'verification/verification_pending.html')
        else:
            return redirect('/verification/get_verified')
    else:
        return redirect('/login')
    


@login_required
def manage_land_posts(request):
    my_land_posts = LandPost.objects.filter(author = request.user)
    return render(request, 'land/manage_land_posts.html', {'my_land_posts':my_land_posts})


@login_required
def delete_land_post(request, post_id):
    post = LandPost.objects.get(id = post_id)
    post.delete()
    return redirect('/land/my-posts')

def secure_land(request, post_id):
    land = LandPost.objects.get(id = post_id )
    phone = land.author.profile.phone_number
    phone = '234'+ str(int(phone))
    message = f"I'm%20interested%20in%20buying%20the%20land:%20{land.size}%20of%20land%20at%20{land.location}%20in%20{land.lga}"
    print("Parameters obtained")
    a = LandDemand.objects.all().first()
    a.demand+=1
    a.save()
    print(LandDemand.objects.all().first().demand)
    return redirect(f'https://wa.me/{phone}?text={message}')


