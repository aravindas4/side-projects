from django import forms
from .models import Expense

class ExpenseForm(forms.Form):
    class Meta:
        models = Expense
        fields = ['expense_name', 'expense_amount', 'expense_mechant_name',
        'expense_category', 'expense_category_item', 'expense_description',]
