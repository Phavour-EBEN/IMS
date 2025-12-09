from django import forms 
from django.forms import ModelForm, widgets
from .models import Product


class ProductForms(ModelForm):
    class Meta:
        mode = Product
        fields = ['name', 'description', 'sku', 'price', 'quantity', 'supplier']
        widgets = {
            'name':forms.
        }