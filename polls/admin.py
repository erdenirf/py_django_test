from django.contrib import admin

from .models import Manufacturer
from .models import Car


# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Car)
