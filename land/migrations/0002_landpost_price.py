# Generated by Django 4.0.3 on 2022-05-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landpost',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
