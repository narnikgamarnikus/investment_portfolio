from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'investment_portfolio.notifications'
    verbose_name = "Telegram Notifications"

    def ready(self):
    	import investment_portfolio.notifications.signals