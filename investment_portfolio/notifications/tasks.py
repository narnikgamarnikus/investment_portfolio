from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import User as TelegramUser, Chat, Bot
from investment_portfolio.users.models import User
import telepot


@shared_task
def send_to_user(user):
	bot = Bot.objects.first()
	telegram_bot = telepot.Bot(bot.api_key)
	telegram_user = TelegramUser.objects.get(user=user)
	if telegram_user.is_authorized:
		chat_id = Chat.objects.get(user=telegram_user)
		reply = 'Отчёт готов. Всё супер!'
		TelegramBot.sendMessage(chat_id, reply)