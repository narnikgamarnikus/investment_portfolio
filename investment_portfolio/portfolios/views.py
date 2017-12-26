from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PortfolioItem, PortfolioTransaction
from .forms import PortfolioItemForm
from djmoney.money import Money


class PortfolioItemDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioItem

    def get_context_data(self, **kwargs):
        context = super(PortfolioItemDetailView, self).get_context_data(**kwargs)
        context['transactions'] = PortfolioTransaction.objects.filter(item=self.object)
        return context

class PortfolioItemUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioItem
    exclude = ['modified', 'created', 'removed']


class PortfolioItemListView(LoginRequiredMixin, ListView):

    model = PortfolioItem


class PortfolioItemCreateView(LoginRequiredMixin, CreateView):

    model = PortfolioItem
    form_class = PortfolioItemForm
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        first_transaction = PortfolioTransaction.objects.create(
                                                item_id = form.instance.id,
                                                invest_date = self.request.POST['invest_date'],
                                                amount = self.request.POST['amount'],
                                                price = Money(
                                                    self.request.POST['price_0'],
                                                    self.request.POST['price_1']
                                                    ),
                                                transaction_type = 'buy')
        return super(PortfolioItemCreateView, self).form_valid(form)


class PortfolioTransactionDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioTransaction


class PortfolioTransactionUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioTransaction
    exclude = ['modified', 'created', 'removed']


class PortfolioTransactionListView(LoginRequiredMixin, ListView):

    model = PortfolioTransaction


class PortfolioTransactionCreateView(LoginRequiredMixin, CreateView):

    model = PortfolioTransaction   