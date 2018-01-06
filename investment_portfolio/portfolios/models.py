from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils import Choices, FieldTracker
from django.conf import settings
from model_utils.fields import StatusField
from investment_portfolio.currencies.models import CurrencyData
from django.utils.timezone import datetime
from djmoney.models.fields import MoneyField


@python_2_unicode_compatible
class Base(SoftDeletableModel, TimeStampedModel):
	
	tracker = FieldTracker()

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Color(Base):
	color = models.CharField(blank=False, null=False, max_length=55, default='#ffffff')
	color_class = models.CharField(blank=False, null=False, max_length=55, default='white') 

	def __str__(self):
		return self.color 


@python_2_unicode_compatible
class PortfolioItem(Base):

	currency = models.ForeignKey('currencies.Currency')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='portfolio_items')
	color = models.ForeignKey(Color, blank=False, null=True)

	@property
	def amount(self):
		total_amount = 0
		for transaction in self.transactions.all():
			total_amount += transaction.amount
		return total_amount

	@property
	def price_usd(self):
		currency_data = CurrencyData.objects.filter(currency=self.currency).last()
		if currency_data:
			return round(currency_data.price_usd * self.amount, 2)
		else:
			import random
			return 1#random.randint(1,9999)

	@property
	def portfolio_percent(self):
		return (self.portfolio_total_amount / 100) * self.price_usd 

	@property
	def profit(self):
		profit = 0
		for transaction in self.transactions.filter(transaction_type = 'buy'):
			profit += transaction.profit
		return profit

	class Meta:
		unique_together = (("user", "currency"),)

	def __str__(self):
		return '{}:{}'.format(
			self.currency.name,
			self.amount
			)

	def get_absolute_url(self):
		return reverse('portfolios:item_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class PortfolioTransaction(Base):
	STATUS = Choices(('buy', _('Buy')), ('sell', _('Sell')))

	transaction_type = StatusField()
	item = models.ForeignKey(PortfolioItem, related_name='transactions', blank=False, null=False)
	amount = models.FloatField(blank=False, null=False)
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	invest_date = models.DateField(blank=False, null=False)

	@property
	def price_usd(self):
		currency_data = CurrencyData.objects.filter(currency=self.item.currency).last()
		if currency_data:
			return self.amount * currency_data.price_usd	
		else:
			import random
			return random.randint(1,9999)

	@property
	def profit(self):
		today = datetime.today()
		#created_currency_date = CurrencyData.objects.filter(created=self.created,
		#											currency=self.item.currency)
		#today_currency_date = CurrencyData.objects.filter(created__gte=self.created,
		#											currency=self.item.currency)
		created_currency_date = 10.000
		today_currency_date = 15.000
		return ((today_currency_date - created_currency_date) / created_currency_date) * 100

	def __str__(self):
		return '{}:{}'.format(
			self.transaction_type,
			self.amount
			)

	def get_absolute_url(self):
		return reverse('portfolios:transaction_detail', kwargs={'pk': self.pk})