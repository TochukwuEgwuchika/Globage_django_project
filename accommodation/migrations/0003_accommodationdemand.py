# Generated by Django 4.0.3 on 2022-05-22 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_alter_accommodationpost_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationDemand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.IntegerField()),
            ],
        ),
    ]