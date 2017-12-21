from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^items$',
        view=views.PortfolioItemListView.as_view(),
        name='item_list'
    ),
    url(
        regex=r'^items/~create/$',
        view=views.PortfolioItemCreateView.as_view(),
        name='item_create'
    ),
    url(
        regex=r'^items/(?P<pk>[\w.@+-]+)/$',
        view=views.PortfolioItemDetailView.as_view(),
        name='item_detail'
    ),
    url(
        regex=r'^items/~update/$',
        view=views.PortfolioItemUpdateView.as_view(),
        name='item_update'
    ),
    url(
        regex=r'^transactions$',
        view=views.PortfolioTransactionListView.as_view(),
        name='transaction_list'
    ),
    url(
        regex=r'^transactions/~create/$',
        view=views.PortfolioTransactionCreateView.as_view(),
        name='transaction_create'
    ),
    url(
        regex=r'^transactions/(?P<pk>[\w.@+-]+)/$',
        view=views.PortfolioTransactionDetailView.as_view(),
        name='transaction_detail'
    ),
    url(
        regex=r'^transactions/~update/$',
        view=views.PortfolioTransactionUpdateView.as_view(),
        name='transaction_update'
    ),    
]
