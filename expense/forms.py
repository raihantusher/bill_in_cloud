from django import forms
from .models import Transaction


class TransactionDebitForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'cat', 'dr']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dr': forms.Textarea(attrs={'class': 'form-control'}),
        }
class TransactionCreditForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'cat', 'cr']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dr': forms.Textarea(attrs={'class': 'form-control'}),
        }
