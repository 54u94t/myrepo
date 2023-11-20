from django import forms
from .models import Product, Expense


class ProductForm(forms.ModelForm):
    # Add a new field for the product category
    category = forms.ChoiceField(
        choices=[
            ('electronics', 'Electronics'),
            ('clothing', 'Clothing'),
            ('books', 'Books'),
            ('addiction', 'Addiction'),
            ('accessories', 'Accessories'),
            ('toys', 'Toys'), 
            ('personal care','Personal Care'),
            # Add more categories as needed
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='electronics',  # Set the default category value
    )

    # Add a default value for the status field
    status = forms.ChoiceField(
        choices=[
            ('acquired', 'Acquired'),
            ('classified', 'Classified'),
            ('on_sale', 'On Sale'),
            ('sold', 'Sold'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='acquired',  # Set the default status value
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image', 'category', 'status']

    # Optional: Add widgets or customize form appearance if needed
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4}),
    }
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category', 'date']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }