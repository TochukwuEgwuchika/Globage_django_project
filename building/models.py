from django.db import models
from accommodation.models import State
from django.contrib.auth.models import User
from django.forms import ModelForm

#Compress image
from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

class BuildingType(models.Model):
    type = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.type}"


class BuildingPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'building_posts')
    category = models.ForeignKey(BuildingType, on_delete=models.CASCADE, related_name = 'buildings', null = True)
    description = models.CharField(max_length=100, help_text='Enter any other information about the building e.g  how stategic the building location is.. ')
    price = models.IntegerField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add = True)
    lga = models.CharField(max_length = 64, null = True, verbose_name = 'City/Town/LGA')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='buildings')
    picture = models.ImageField(upload_to = 'building_pics', null = True)

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

        super(BuildingPost, self).save() 



class BuildingPostForm(ModelForm):
    class Meta:
        model = BuildingPost
        fields = ['picture','category','description','location', 'lga', 'state', 'price']

class BuildingDemand(models.Model):
    demand = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.demand}'