import requests
import datetime
from .models import Currency, CurrencyData
from celery.task.base import periodic_task

@periodic_task(run_every=datetime.timedelta(seconds=60*60))
def parse_currencies():	
	
	response = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')
	
	for currency in response.json():
		print(currency)
		new_currency, created = Currency.objects.get_or_create(name = currency['id'],
															   symbol = currency['symbol'])
		currency_date = CurrencyData.objects.create(currency = new_currency,
													rank = currency['rank'],
													price_usd = currency['price_usd'],
													price_btc = currency['price_btc'],
													daily_volume_usd = currency['24h_volume_usd'],
													market_cap_usd = currency['available_supply'],
													available_supply = currency['available_supply'],
													total_supply = currency['total_supply'],
													max_supply = currency['max_supply'],
													percent_change_1h = currency['percent_change_1h'],
													percent_change_24h = currency['last_updated'],
													percent_change_7d = currency['last_updated'],
													last_updated = currency['last_updated'])