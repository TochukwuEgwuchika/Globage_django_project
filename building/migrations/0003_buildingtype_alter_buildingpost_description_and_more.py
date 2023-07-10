# Generated by Django 4.0.3 on 2022-05-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_alter_buildingpost_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='buildingpost',
            name='description',
            field=models.CharField(help_text='Enter any other information about the building e.g  how stategic the building location is.. ', max_length=100),
        ),
        migrations.AddField(
            model_name='buildingpost',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='building.buildingtype'),
        ),
    ]
