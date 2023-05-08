from django import forms
from .models import Transaction,Category


class TransactionDebitForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label=' Category')
    dr = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Debit amount(00.00)'}),label=' Amount')
    class Meta:
        model = Transaction
        fields = ['title', 'cat', 'dr']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Expense Title'})
        }
class TransactionCreditForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Category')
    cr = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Debit amount(00.00)'}),label='Amount')
    
    class Meta:
        model = Transaction
        fields = ['title', 'cat', 'cr']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
