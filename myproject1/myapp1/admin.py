from django.contrib import admin
from .models import Car, Brand, Vehicle, BrandFr

# Register your models here.

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(BrandFr)