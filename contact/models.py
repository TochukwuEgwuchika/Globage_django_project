from django.db import models


# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length = 70, verbose_name = 'Your Name')
    sender_mail = models.EmailField(max_length=254, verbose_name = 'Your Email')
    sender_phone = models.CharField(max_length=20, verbose_name = 'Your Phone Number')
    message = models.TextField(verbose_name = 'Your Message')

    def __str__(self):
        return f"Message from {self.sender}"



