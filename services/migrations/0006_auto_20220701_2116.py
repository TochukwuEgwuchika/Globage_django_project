# Generated by Django 3.2.13 on 2022-07-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20220630_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepersonnel',
            name='service_provided',
        ),
        migrations.AddField(
            model_name='servicepersonnel',
            name='skills',
            field=models.ManyToManyField(to='services.Service'),
        ),
    ]