from django.shortcuts import render, redirect
from .models import Message

# Create your views here.

def contact(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        sender_mail = request.POST['senderEmail']
        sender_phone = request.POST['senderPhone']
        message = request.POST['message']
        Message.objects.create(sender = sender, sender_mail = sender_mail, sender_phone = sender_phone, message = message)
        return redirect('/home')
    return render(request, 'contact/contact.html')

