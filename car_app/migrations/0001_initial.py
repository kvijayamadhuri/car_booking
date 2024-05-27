# Generated by Django 5.0.3 on 2024-03-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('body_style', models.CharField(max_length=30)),
                ('fuel_type', models.CharField(max_length=10)),
                ('seating_capacity', models.CharField(max_length=10)),
                ('transmission_type', models.CharField(max_length=10)),
                ('price_per_hour', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
            ],
        ),
    ]