from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PortfolioItem, PortfolioTransaction


class PortfolioItemDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioItem


class PortfolioItemUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioItem
    exclude = ['modified', 'created', 'removed']


class PortfolioItemListView(LoginRequiredMixin, ListView):
    model = PortfolioItem


class PortfolioItemCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioItem



class PortfolioTransactionDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioTransaction


class PortfolioTransactionUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioTransaction
    exclude = ['modified', 'created', 'removed']


class PortfolioTransactionListView(LoginRequiredMixin, ListView):
    model = PortfolioTransaction


class PortfolioTransactionCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioTransaction   