from django.contrib import admin
from .models import Listing, CarMake, CarModel


# Register your models here.
admin.site.register(Listing)
admin.site.register(CarMake)
admin.site.register(CarModel)
