from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import ModelForm

#Compress image
from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.


class AccommodationType(models.Model):
    type = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.type}"

class State(models.Model):
    state_name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.state_name}"

class AccommodationPost(models.Model):
    category = models.ForeignKey(AccommodationType, on_delete=models.CASCADE, related_name = 'accommodation_type')
    description = models.TextField(help_text = 'Provide more details like number of rooms')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'accommodation_posts')
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to = 'accommodation_pics', blank = True, default ='default_accommodation' )
    date_posted = models.DateTimeField(auto_now_add = True, blank = True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='accommodations')
    lga = models.CharField(max_length = 64, null=True, verbose_name = 'Local Government Area/Town/City')

    def __str__(self):
        return f"Accommodation {self.id}:House at {self.location} in {self.state}"

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.picture)

        output = BytesIO()

        original_width, original_height = im.size
        aspect_ratio = round(original_width / original_height)
        desired_height = 1000  # Edit to add your desired height in pixels
        desired_width = desired_height * aspect_ratio

        # Resize the image
        im = im.resize((desired_width, desired_height))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.picture = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.picture.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(AccommodationPost, self).save() 

    

    


class AccommodationPostForm(ModelForm):
    class Meta:
        model = AccommodationPost
        fields = ['category', 'description', 'location', 'lga', 'state', 'picture']


class AccommodationDemand(models.Model):
    demand = models.IntegerField(default = 0)
    def __str__(self):
        return f'{self.demand}'
