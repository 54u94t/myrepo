from django import forms
from .models import Product, Expense

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category', 'date']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }