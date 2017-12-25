from django.dispatch import receiver

from django.db.models.signals import pre_save, post_save
from .models import PortfolioItem, PortfolioTransaction

'''
@receiver(post_save, sender=PortfolioTransaction)
def change_portfolio_item_data(sender, instance, created, **kwargs):

	if instance.transaction_type == 'buy':
		instance.item.amount += instance.amount
	else:
		instance.item.amount -= instance.amount

	instance.item.save()


@receiver(post_save, sender=PortfolioItem)
def create_first_portfolio_transaction(sender, instance, created, **kwargs):
	if created:
		first_transaction = PortfolioTransaction.objects.create(
										item=instance,
										amount=instance.amount,
										transaction_type='buy',
										created=instance.invest_date
										)
'''