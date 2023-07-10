from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class UserVerification(models.Model):
    CHOICES = [('Unverified','Unverified'), ('Pending', 'Pending'), ('Verified', 'Verified')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_status = models.CharField(max_length = 10, choices = CHOICES, default = 'Unverified')
    id_card = models.ImageField(upload_to='verification', help_text = "Upload a valid ID Card (National ID card, Voter's Card or Driver's License", verbose_name = 'Valid ID Card')
    passport = models.ImageField(upload_to = 'verification', help_text = 'Upload a picture of your passport photograph', verbose_name = 'Passport Photograph')
    is_payment_up_to_date = models.BooleanField( default = False )

    def __str__(self):
        return f"{self.user.username} : {self.verification_status}"

class UserVerificationForm(ModelForm):
    class Meta:
        model = UserVerification
        fields = ['id_card', 'passport']


@receiver(post_save, sender=User)
def create_user_userverification(sender, instance, created, **kwargs):
    if created:
        UserVerification.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_userverification(sender, instance, **kwargs):
    instance.userverification.save()