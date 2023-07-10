from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accommodation.models import State
from django.forms import ModelForm
from django import forms


class Profile(models.Model):
    CHOICES = (('Agent', 'Agent'), ('Service Personnel', 'Service Personnel'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to ='profile_pics', default = 'default.jpg')
    date_of_birth = models.DateField(null = True)
    phone_number = models.CharField(max_length=11, null = True, verbose_name = 'Phone Number: +234', help_text = 'Preferably, your whatsapp number!')
    residential_address = models.TextField(max_length=500, null = True)
    permanent_address = models.TextField(max_length=500, null = True)
    state_of_origin = models.ForeignKey(State,on_delete= models.CASCADE, null = True)
    nationality = models.CharField(max_length=30, null = True)
    is_service_personnel = models.BooleanField(default = False)
    is_service_personnel_registered = models.BooleanField(default = False)
    is_agent = models.BooleanField(default=False)
    
    registered_as = models.CharField(max_length = 50, choices = CHOICES, null = True, verbose_name='Register as')

    def __str__(self):
        return f'{self.user.username} Profile'
  

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture','date_of_birth', 'phone_number', 'residential_address', 'permanent_address', 'state_of_origin', 'nationality', 'registered_as')
        widgets = {'date_of_birth': DateInput()}