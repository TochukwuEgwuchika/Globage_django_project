# Generated by Django 4.0.3 on 2022-05-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_service_personnel',
            field=models.BooleanField(default=False),
        ),
    ]