from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import os
from .forms import ProductForm
from .models import Product

def home_view(request):
    return render(request, 'home.html')

def dash_view(request):
    prod = Product.objects.all()
    context = {'prod': prod}
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