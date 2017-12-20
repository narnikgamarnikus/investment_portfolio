from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Currency, CurrencyData


class CurrencyDetailView(LoginRequiredMixin, DetailView):
    model = Currency
    # These next two lines tell the view to index lookups by name
    slug_field = 'name'
    slug_url_kwarg = 'name'


class CurrencyListView(LoginRequiredMixin, ListView):
    model = Currency
    # These next two lines tell the view to index lookups by name
    slug_field = 'name'
    slug_url_kwarg = 'name'


class CurrencyDataDetailView(LoginRequiredMixin, DetailView):
    model = CurrencyData
    # These next two lines tell the view to index lookups by pk
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class CurrencyDataListView(LoginRequiredMixin, ListView):
    model = CurrencyData
    # These next two lines tell the view to index lookups by pk
    slug_field = 'pk'
    slug_url_kwarg = 'pk'