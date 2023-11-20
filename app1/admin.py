from django.contrib import admin
from .models import Product, Expense
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')  # Replace with actual fields
    search_fields = ('name',)  # Add fields you want to be searchable

# Add more configurations or customize as needed
@admin.register(Expense)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount', 'category')  # Replace with actual fields
    search_fields = ('name',)  # Add fields you want to be searchable
