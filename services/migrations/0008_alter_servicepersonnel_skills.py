# Generated by Django 3.2.13 on 2022-07-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_servicepersonnel_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepersonnel',
            name='skills',
            field=models.ManyToManyField(to='services.Service'),
        ),
    ]
