from django.db import models
from accommodation.models import State
from django.contrib.auth.models import User
from django.forms import ModelForm



# Create your models here.

class LandPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'land_posts')
    size = models.CharField(max_length=64, help_text= 'How many plots, acres or hectares?')
    price = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=100, help_text = 'Give a detailed location')
    date_posted = models.DateTimeField(auto_now_add = True)
    lga = models.CharField(max_length = 64, null = True, verbose_name='LGA / Town / City')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='lands')

    def __str__(self):
        return f"{self.size} of land at {self.lga}"


class LandDemand(models.Model):
    demand = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.demand}'


class LandPostForm(ModelForm):
    class Meta:
        model = LandPost
        fields = ['size','price', 'location', 'lga', 'state']