from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils import Choices, FieldTracker
from django.conf import settings
from model_utils.fields import StatusField


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
	item = models.ForeignKey(PortfolioItem, blank=False, null=False)
	amount = models.FloatField(blank=False, null=False)


	def __str__(self):
		return '{}:{}'.format(
			self.transaction_type,
			self.amount
			)

	def get_absolute_url(self):
		return reverse('portfolios:transaction_detail', kwargs={'pk': self.pk})