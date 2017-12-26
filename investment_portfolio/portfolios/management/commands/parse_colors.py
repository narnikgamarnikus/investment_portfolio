import logging
import requests
from bs4 import BeautifulSoup
from ...models import Color

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
	help = 'Parse colors from mdbootstrap.com/css/colors'

	def handle(self, *args, **options):

		response = requests.get('https://mdbootstrap.com/css/colors/')
		soup = BeautifulSoup(response.text, 'html.parser')
		colors = soup.find('div', 'dynamic-color')

		for color in colors.find_all('p'):
			split_color = color.text.split(' ')
			if split_color[0][0] == '#':				
				color = split_color[0]
				split_color.remove(color)
				color_class = ' '.join(split_color)
				new_color, created = Color.objects.get_or_create(
					color = color,
					color_class = color_class
					)
			if created:
				logger.info("Color %d create successfull", color_class)