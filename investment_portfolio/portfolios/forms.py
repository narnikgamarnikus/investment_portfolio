from django import forms
from .models import PortfolioItem
from investment_portfolio.currencies.models import Currency

class PortfolioItemForm(forms.ModelForm):

	invest_date = forms.DateField()

	class Meta:
		model = PortfolioItem
		fields = ['currency', 'amount', 'invest_date']


	def __init__(self, *args, **kwargs):
		super(PortfolioItemForm, self).__init__(*args, **kwargs)
		self.fields['currency'].queryset = Currency.objects.all()