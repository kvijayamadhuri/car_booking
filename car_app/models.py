from django.db import models
from django.utils import timezone
from users.models import User


class Car(models.Model):
    model=models.CharField(max_length=30)
    body_style=models.CharField(max_length=30)
    fuel_type=models.CharField(max_length=10)
    seating_capacity=models.CharField(max_length=10)
    transmission_type=models.CharField(max_length=10)
    price_per_hour=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to="profile_pic",blank=True)
    is_booked=models.BooleanField(default=False)
    book_now=models.BooleanField(default=True)
    