# Generated by Django 4.0.3 on 2022-05-03 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_status', models.CharField(choices=[('Unverified', 'Unverified'), ('Pending', 'Pending'), ('Verified', 'Verified')], default='Unverified', max_length=10)),
                ('id_card', models.ImageField(help_text="Upload a valid ID Card (National ID card, Voter's Card or Driver's License", upload_to='verification', verbose_name='Valid ID Card')),
                ('passport', models.ImageField(help_text='Upload a picture of your passport photograph', upload_to='verification', verbose_name='Passport Photograph')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]