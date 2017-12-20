from django.dispatch import receiver

from django.db.models.signals import pre_save, post_save
from .models import PortfolioItem, PortfolioTransaction

@receiver(post_save, sender=PortfolioTransaction)
def change_portfolio_item_data(sender, instance, created, **kwargs):
	
	if instance.transaction_type == 'buy':
		instance.item.amount += instance.amount
	else:
		instance.item.amount -= instance.amount

	instance.item.save()
