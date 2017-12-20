from django.contrib import admin
from .models import PortfolioItem, PortfolioTransaction

admin.site.register(PortfolioItem)
admin.site.register(PortfolioTransaction)