from django import forms
from .models import ExpensesList


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpensesList
        fields = ['expense_category', 'amount_of_money', 'entry_date', 'description']
        widgets = {
            'expense_category': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_of_money': forms.NumberInput(attrs={'class': 'form-control'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
