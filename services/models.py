from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from accommodation.models import State
from django import forms

# Create your models here.

class RangeOfCoverage(models.Model):
    ranges = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.ranges}"

class Service(models.Model):
    name_of_service = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.name_of_service}"
        
class WorkSample(models.Model):
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'work_samples', null = True, blank = True)

class ServicePersonnel(models.Model):
    service_personnel = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provided = models.ForeignKey(Service, on_delete=models.CASCADE, null = True)
    range_of_coverage = models.ForeignKey(RangeOfCoverage, on_delete=models.CASCADE ,help_text='Around what area can you provide your service? Within your state or Nationwide or other', related_name='service_personnels')
    location = models.CharField(max_length = 100, help_text="Give details on range of coverage. Like:'Entire State','Eastern  Nigeria', etc.")
    state_of_residence = models.ForeignKey(State, on_delete=models.CASCADE)
    #cover_letter = models.CharField(max_length = 100, help_text= 'What makes you different from other service personnels in your category')
    date_became_service_personnel = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_personnel.first_name} {self.service_personnel.last_name}: {self.service_provided}"


class ServicePersonnelForm(ModelForm):
    class Meta:
        model = ServicePersonnel
        fields = ['state_of_residence','service_provided', 'location', 'range_of_coverage']


class ServicePersonnelDemand(models.Model):
    demand = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.demand}'



