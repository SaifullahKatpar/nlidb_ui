from django.contrib import admin

from .models import Transformer, ElectricityBill

admin.site.register(Transformer)
admin.site.register(ElectricityBill)
