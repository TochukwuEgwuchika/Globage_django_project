# Generated by Django 4.0.3 on 2022-05-03 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accommodation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeOfCoverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranges', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_service', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePersonnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='Give details on range of coverage', max_length=100)),
                ('cover_letter', models.CharField(help_text='What makes you different from other service personnels in your category', max_length=100)),
                ('date_became_service_personnel', models.DateField(auto_now_add=True)),
                ('range_of_coverage', models.ForeignKey(help_text='Around what area can you provide your service? Within your state or Nationwide or other', on_delete=django.db.models.deletion.CASCADE, related_name='service_personnels', to='services.rangeofcoverage')),
                ('service_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_provided', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('state_of_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.state')),
            ],
        ),
    ]