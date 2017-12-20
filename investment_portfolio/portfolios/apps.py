from django.apps import AppConfig


class PortfoliosConfig(AppConfig):
    name = 'investment_portfolio.portfolios'
    verbose_name = "Portfolios"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
