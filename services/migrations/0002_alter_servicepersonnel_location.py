# Generated by Django 4.0.3 on 2022-05-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepersonnel',
            name='location',
            field=models.CharField(help_text="Give details on range of coverage. Like:'Entire State','Eastern  Nigeria', etc.", max_length=100),
        ),
    ]
