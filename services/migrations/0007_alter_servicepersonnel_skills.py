# Generated by Django 3.2.13 on 2022-07-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20220701_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepersonnel',
            name='skills',
            field=models.ManyToManyField(null=True, to='services.Service'),
        ),
    ]
