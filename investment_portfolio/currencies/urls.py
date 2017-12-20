from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.CurrencyListView.as_view(),
        name='currency_list'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/$',
        view=views.CurrencyDetailView.as_view(),
        name='currency_detail'
    ),
    url(
        regex=r'^$',
        view=views.CurrencyDataListView.as_view(),
        name='currency_data_list'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/$',
        view=views.CurrencyDataDetailView.as_view(),
        name='currency_data_detail'
    ),
]
