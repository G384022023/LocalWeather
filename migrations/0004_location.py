# Generated by Django 5.1 on 2024-10-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocalWeather', '0003_weather_delete_currentconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
    ]
