from django.apps import AppConfig


class CurrenciesConfig(AppConfig):
    name = 'investment_portfolio.currencies'
    verbose_name = "Currencies"

    def ready(self):
        pass
