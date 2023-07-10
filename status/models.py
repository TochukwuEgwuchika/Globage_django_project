from django.db import models

# Create your models here.


class Passphrase(models.Model):
    passphrase = models.CharField(max_length=20)
