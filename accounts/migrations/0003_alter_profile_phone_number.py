# Generated by Django 4.0.3 on 2022-05-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_is_service_personnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(help_text='Preferably, your whatsapp number!', max_length=11, null=True, verbose_name='Phone Number: +234'),
        ),
    ]