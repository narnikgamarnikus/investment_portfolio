import telepot
import string, random
from django.db import models
from django.conf import settings
from annoying.fields import AutoOneToOneField
from django.utils.translation import ugettext as _
from django.utils.functional import cached_property
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Bot(models.Model):
	api_key = models.CharField(max_length=255, verbose_name=_('API_KEY'))
	bot_id = models.CharField(max_length=255, verbose_name=_('id'))
	first_name = models.CharField(max_length=255, verbose_name=_('first_name'))
	username = models.CharField(max_length=255, verbose_name=_('first_name'))

	@cached_property
	def get_me(self):
		bot = telepot.Bot(self.api_key)
		data = bot.getMe()
		self.id = data['id']
		self.first_name = data['first_name']
		self.username = data['username']
		return data

	@staticmethod
	def sendMessage(self, chat_id, payload):
		TelegramBot = telepot.Bot(self.api_key)
		TelegramBot.sendMessage(chat_id, payload)

	def save(self, *args, **kwargs):
		if not self.pk:
			self.get_me
			TelegramBot = telepot.Bot(self.api_key)
			TelegramBot.setWebhook('xn------dddfnxoenlfghchl4bitc.xn--90ais/notifications/{bot_token}/'.format(bot_token=self.api_key))
		return super(Bot, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('Bot')
		verbose_name_plural = _('Bots')

	def __str__(self):
		return '%s' % str(self.first_name)


@python_2_unicode_compatible
class User(models.Model):
	user = AutoOneToOneField(settings.AUTH_USER_MODEL, null=True, verbose_name=_('user'))
	unique_code = models.CharField(max_length=255, verbose_name=_('unique code'))
	is_authorized = models.BooleanField(default=False, verbose_name=_('Is authorized'))

	@property
	def generate_unique_code(self, size=36, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
		unique_code = ''.join(random.choice(chars) for _ in range(size))
		return unique_code

	@property
	def set_unique_code(self):
		self.unique_code = self.generate_unique_code

	@property
	def check_unique_code(self, code):
		if self.unique_code == code:
			return True
		return False

	def save(self, *args, **kwargs):
		if not self.pk or not self.unique_code:
			self.set_unique_code
		return super(User, self).save(*args, **kwargs)


	def __str__(self):
		return '%s' % str(self.user.username)


@python_2_unicode_compatible
class Chat(models.Model):
	chat_id = models.CharField(max_length=255, verbose_name='chat id')
	user = models.ForeignKey('notifications.User', null=True)

@python_2_unicode_compatible
class Message(models.Model):
	chat_id = models.ForeignKey('notifications.Chat', null=True, verbose_name=_('chat id'))
	text = models.CharField(max_length=255, verbose_name=_('text'))
	message_id = models.CharField(max_length=255, verbose_name=_('message id'))