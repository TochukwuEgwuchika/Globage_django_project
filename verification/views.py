from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from verification.models import UserVerificationForm, UserVerification
from django.contrib.auth.models import User

# Create your views here.

@login_required
def user_verification(request):
    if request.method == 'POST':
        user = request.user
        form = UserVerificationForm(request.POST, request.FILES, instance = user.userverification)
        if form.is_valid():
            verification = form.save(commit = False)
            verification.verification_status = 'Pending'
            print(verification.verification_status)
            
            verification.save()
            if verification.verified_as == 'Service Personnel':
                user.profile.is_service_personnel = True
                user.save()

            elif verification.verified_as == 'Agent':
                user.profile.is_agent = True
                user.save()
            return redirect('/dashboard')
        
    form = UserVerificationForm()       
    return render(request, 'verification/user_verification_form.html', {'form': form})
