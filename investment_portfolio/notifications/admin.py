from django.contrib import admin
from .models import Bot, User as TelegramUser

@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
	fields = ['api_key']
	
admin.site.register(TelegramUser)