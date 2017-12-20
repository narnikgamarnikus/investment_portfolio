from django.contrib import admin
from .models import Currency, CurrencyData


admin.site.register(Currency)
admin.site.register(CurrencyData)