from .models import Customer, Items, Kysha
from django import forms


class CustomerForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50)

    class Meta:
        model = Customer
        fields = ('full_name',)