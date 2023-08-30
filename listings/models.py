from django.db import models
from django_resized import ResizedImageField
from django.conf import settings
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
        max_length=10, choices=choices.get_year_choices(), null=True)
    mileage = models.IntegerField(null=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, choices=choices.COUNTIES)
    body_type = models.CharField(
        max_length=100, choices=choices.BODY_TYPE, null=True, blank=True)
    fuel_type = models.CharField(max_length=100, choices=choices.FUEL_TYPE)
    engine_size = models.CharField(
        max_length=20, choices=choices.ENGINE_SIZES)
    transmission = models.CharField(
        max_length=100, choices=choices.TRANSMISSION)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    listing_image_1 = ResizedImageField(
        quality=75, force_format='WEBP', blank=True,
        upload_to='listings/', default='listings/default-listing-img.jpg')
    listing_image_2 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    listing_image_3 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    listing_image_4 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    listing_image_5 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    listing_image_6 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    listing_image_7 = ResizedImageField(
        quality=75, force_format='WEBP', upload_to='listings/', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.car_make)

    @property
    def listing_title(self):
        if self.car_make and self.car_model:
            return f'{self.car_make.name} {self.car_model.name}'
        else:
            return "Untitled Listing"

    @property
    def listing_main_img(self):
        if self.listing_image_1:
            url = self.listing_image_1.url
        else:
            url = (
                settings.STATIC_URL +
                'images/listings/default-listing-img.jpg'
            )
        return url


class Favourite(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.listing)
