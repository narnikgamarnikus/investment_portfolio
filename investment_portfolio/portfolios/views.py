from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PortfolioItem, PortfolioTransaction
from .forms import PortfolioItemForm

class PortfolioItemDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioItem


class PortfolioItemUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioItem
    exclude = ['modified', 'created', 'removed']


class PortfolioItemListView(LoginRequiredMixin, ListView):

    model = PortfolioItem


class PortfolioItemCreateView(LoginRequiredMixin, CreateView):

    model = PortfolioItem
    #fields = ['currency', 'amount', 'invest_date']
    form_class = PortfolioItemForm
    
    def form_valid(self, form):
        #print(self.request.POST)
        
        form.instance.user_id = self.request.user.id
        form.instance.invest_date = self.request.POST['invest_date_submit']
        print(self.request.POST['invest_date_submit'])
        print(form.instance)
        
        return super(PortfolioItemCreateView, self).form_valid(form)

    def form_invalid(self, form):
        #print(self.request.POST)
        return super(PortfolioItemCreateView, self).form_invalid(form)



class PortfolioTransactionDetailView(LoginRequiredMixin, DetailView):
    
    model = PortfolioTransaction


class PortfolioTransactionUpdateView(LoginRequiredMixin, UpdateView):

    model = PortfolioTransaction
    exclude = ['modified', 'created', 'removed']


class PortfolioTransactionListView(LoginRequiredMixin, ListView):

    model = PortfolioTransaction


class PortfolioTransactionCreateView(LoginRequiredMixin, CreateView):

    model = PortfolioTransaction   