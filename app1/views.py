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


def home_view(request):
    return render(request, 'home.html')

def store_view(request):
    return render(request, 'store.html')
def about_view(request):
    return render(request, 'about.html')

def dash_view(request):
    # Get products and expenses data
    products = Product.objects.all()
    expenses_table = Expense.objects.all()  # Retrieve all expenses directly

    # Extract data for the bar chart
    product_names = [product.name for product in products]
    product_quantities = [product.quantity for product in products]

    # Group expenses by category and sum amounts
    grouped_expenses = Expense.objects.values('category').annotate(total_amount=Sum('amount'))

    expense_categories = [expense['category'] for expense in grouped_expenses]
    expense_amounts = [expense['total_amount'] for expense in grouped_expenses]

    # Plot the bar chart for products with smaller width
    plt.figure(figsize=(8, 4))
    plt.plot(product_names, product_quantities, marker='o', color='blue', linestyle='-')  # Use plt.plot for line chart
    plt.xlabel('Product Names')
    plt.ylabel('Product Quantity')
    plt.title('Products Line Chart')
    plt.xticks(rotation=50, ha='right')
    plt.tight_layout(pad=4.0)

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the plot image to base64
    chart_image_path_bar = base64.b64encode(buffer.read()).decode('utf-8')

    # Plot the pie chart for expenses with aggregated amounts
    plt.figure(figsize=(5, 2.5))
    plt.pie(expense_amounts, labels=expense_categories, autopct='%1.1f%%', startangle=90,
            colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expenses Pie Chart')

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

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to another page
            return redirect('dash_view')
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