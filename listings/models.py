from django.db import models
from . import choices
from users.models import Profile
import uuid


class CarMake(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class CarModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Listing(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    car_make = models.ForeignKey(
        CarMake, on_delete=models.SET_NULL, null=True, blank=True)
    car_model = models.ForeignKey(
        CarModel, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
    year = models.CharField(
        max_length=10, choices=choices.get_year_choices(), null=True,
        blank=True)
    price = models.IntegerField()
    mileage = models.IntegerField(null=True, blank=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, choices=choices.COUNTIES)
    body_type = models.CharField(
        max_length=100, choices=choices.BODY_TYPE, null=True, blank=True)
    fuel_type = models.CharField(max_length=100, choices=choices.FUEL_TYPE)
    engine_size = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True)
    battery_capacity = models.IntegerField(null=True, blank=True)
    transmission = models.CharField(
        max_length=100, choices=choices.TRANSMISSION)
    created = models.DateField(auto_now_add=True)
    listing_image_1 = models.ImageField(
        null=True, blank=True, default='default-listing-img.jpg')
    listing_image_2 = models.ImageField(null=True, blank=True)
    listing_image_3 = models.ImageField(null=True, blank=True)
    listing_image_4 = models.ImageField(null=True, blank=True)
    listing_image_5 = models.ImageField(null=True, blank=True)
    listing_image_6 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.car_make)

    @property
    def listing_title(self):
        return f'{self.car_make} {self.car_model}'
