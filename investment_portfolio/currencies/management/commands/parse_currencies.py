import logging
import requests
from ...models import Currency

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
	help = 'Parse currencies from coinmarketcup.com'

	def handle(self, *args, **options):

		response = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')

		for currency in response.json():
			new_currency, created = Currency.objects.get_or_create(
				name = currency['id'],
				symbol = currency['symbol']
				)

			if created:
				logger.info("Currency %d create successfull", new_currency.name)