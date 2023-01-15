from django import forms
from .models import Expense


class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'price')
