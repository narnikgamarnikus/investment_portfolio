from django.dispatch import receiver
from django.db.models.signals import post_save
from investment_portfolio.users.models import User
from .models import User as TelegramUser


@receiver(post_save, sender=User)
def create_or_update_clientprofile(sender, instance, created, **kwargs):
	if created:
		TelegramUser.objects.create(user=instance)