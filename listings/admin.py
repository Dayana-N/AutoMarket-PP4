from django.contrib import admin
from .models import Listing, CarMake, CarModel, Favourite


# Register your models here.
admin.site.register(Listing)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Favourite)
