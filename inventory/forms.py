from django import forms 
from django.forms import ModelForm
from .models import Product


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'sku', 'price', 'quantity', 'supplier']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'eg: laptop bag', 'class':'form-control'}),
            'description':forms.TextInput(attrs={'placeholder':'eg: portable bag to give laptops safe', 'class':'form-control'}),
            'sku':forms.TextInput(attrs={'placeholder':'eg: SG123', 'class':'form-control'}),
            'price':forms.TextInput(attrs={'placeholder':'eg: 20.99', 'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'placeholder':'eg: 12', 'class':'form-control'}),
            'supplier':forms.TextInput(attrs={'placeholder':'eg: sk enterp.', 'class':'form-control'}),
        }