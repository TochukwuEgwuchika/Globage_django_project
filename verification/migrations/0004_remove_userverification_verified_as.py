# Generated by Django 3.2.13 on 2022-06-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0003_userverification_is_payment_up_to_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userverification',
            name='verified_as',
        ),
    ]