# Generated by Django 4.0.3 on 2022-05-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_landdemand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landdemand',
            name='demand',
            field=models.IntegerField(default=0),
        ),
    ]
