from django.apps import AppConfig


class CurrenciesConfig(AppConfig):
    name = 'investment_portfolio.currencies'
    verbose_name = "Currencies"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
