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


@python_2_unicode_compatible
class Base(SoftDeletableModel, TimeStampedModel):
	
	tracker = FieldTracker()

	class Meta:
		abstract = True


@python_2_unicode_compatible
class PortfolioItem(Base):

	currency = models.ForeignKey('currencies.Currency')
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	amount = models.FloatField(blank=False, null=False)
	invest_date = models.DateField(blank=False, null=False)

	@property
	def price_usd(self):
		current_usd_price = CurrencyData.objects.filter(currency=self.currency).last()
		return current_usd_price * self.amount


	@property
	def portfolios_total_amount(self):
		total_amount = 0
		for item in PortfolioItem.objects.all():
			total_amount += item.current_usd_price
		return total_amount

	@property
	def portfolio_percent(self):
		return (self.portfolio_total_amount / 100) * self.price_usd 

	@property
	def profit(self):
		profit = 0
		print(self.transactions)
		for transaction in self.transactions.filter(transaction_type = 'buy'):
			profit += transaction.amount
		print(profit)
		return profit

	@property
	def dataset(self):
		import random
		return [random.randint(i, 50) for i in range(7)]
		#return [data.price_usd * self.amount for data in CurrencyData.objects.filter(currency=self.currency)]

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