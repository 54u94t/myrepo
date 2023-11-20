from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm, ExpenseForm
from .models import Product, Expense
import os
import threading
import matplotlib
from django.conf import settings
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
from django.db.models import Sum
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
import base64
import io
from django.utils.text import slugify
from django.urls import reverse

def home_view(request):
    return render(request, 'home.html')

def store_view(request):
    items = Product.objects.all()
    context = {'items': items}
    return render(request, 'store.html', context)
def about_view(request):
    return render(request, 'about.html')

import io
import base64
import matplotlib.pyplot as plt
from django.db.models import Sum
from django.shortcuts import render
from .models import Product, Expense

def dash_view(request):
    # Get products and expenses data
    products = Product.objects.all()
    expenses_table = Expense.objects.all()

    # Extract data for the bar chart
    product_names = [product.name for product in products]
    product_quantities = [product.quantity for product in products]

    # Extract data for the line chart
    product_prices = [product.price for product in products]

    # Group expenses by category and sum amounts
    grouped_expenses = Expense.objects.values('category').annotate(total_amount=Sum('amount'))

    expense_categories = [expense['category'] for expense in grouped_expenses]
    expense_amounts = [expense['total_amount'] for expense in grouped_expenses]

    # Plot the bar chart for products with smaller width
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot the line chart for product prices
    ax1.plot(product_names, product_prices, marker='o', color='red', linestyle='-', label='Product Prices')

    # Create a second y-axis to plot the bar chart for product quantities
    ax2 = ax1.twinx()
    ax2.bar(product_names, product_quantities, color='blue', alpha=0.5, label='Product Quantities')

    # Set labels and title
    ax1.set_xlabel('Product Names')
    ax1.set_ylabel('Product Prices', color='red')
    ax2.set_ylabel('Product Quantities', color='blue')
    ax1.set_title('Products Line and Bar Chart')
    ax1.set_xticks(product_names)
    ax1.tick_params(axis='x', rotation=50)  # Update this line
    ax1.legend(loc='upper left', bbox_to_anchor=(0.7, 1.0))
    ax2.legend(loc='upper left', bbox_to_anchor=(0.7, 0.9))

    plt.tight_layout(pad=4.0)

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the plot image to base64
    chart_image_path_bar = base64.b64encode(buffer.read()).decode('utf-8')

    # Plot the pie chart for expenses with aggregated amounts
    plt.figure(figsize=(8, 4))
    plt.pie(expense_amounts, labels=expense_categories, autopct='%1.1f%%', startangle=90,
            colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the plot image to base64
    chart_image_path_pie = base64.b64encode(buffer.read()).decode('utf-8')

    # Pass chart image paths, expenses, and products to the context
    context = {
        'prod': products,
        'chart_image_path_bar': f"data:image/png;base64,{chart_image_path_bar}",
        'chart_image_path_pie': f"data:image/png;base64,{chart_image_path_pie}",
        'expenses': grouped_expenses,
        'expenses_table': expenses_table  # Include grouped expenses in the context
    }

    return render(request, 'dashboard.html', context)

def product_image_filename(instance, filename):
    # Get the product name from the instance
    product_name = instance.name

    # Generate a slug from the product name to ensure a valid filename
    slug = slugify(product_name)

    # Get the file extension from the original filename
    _, file_extension = os.path.splitext(filename)

    # Construct the new filename with the slug and original file extension
    new_filename = f"{slug}{file_extension}"

    # Return the complete path for storing the image
    return os.path.join('your_upload_path', new_filename)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store_view')  # Redirect to your desired view after a successful form submission
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_view')  # Redirect to a view displaying the list of expenses
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def manage_prod_view(request):
    products = Product.objects.all()  # Assuming your model is named TestProduct
    context = {'products': products}
    return render(request, 'prodmgr.html', context)
def update_status(request, product_id, new_status):
    product = get_object_or_404(Product, pk=product_id)
    
    # Update the product status
    product.status = new_status
    product.save()

    # Redirect to the 'store_view' instead of 'product_detail'
    return redirect('store_view')