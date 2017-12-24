from django.apps import AppConfig


class PortfoliosConfig(AppConfig):
    name = 'investment_portfolio.portfolios'
    verbose_name = "Portfolios"

    def ready(self):
    	import investment_portfolio.portfolios.signals
