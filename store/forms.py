from django import forms
from .models import Customer
from .models import Item

# store/forms.py
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_number', 'name', 'balance']  # Include customer_number
        widgets = {
            'customer_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Customer Number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Item Price'}),
        }
        
class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Select CSV file')