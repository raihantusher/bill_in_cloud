from django import forms
from .models import CustomerProfile, Package


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"
