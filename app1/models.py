from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Expense(models.Model):
    category_choices = [
        ('Groceries', 'Groceries'),
        ('Outside_Food', 'Outside_Food'),
        ('Clothing', 'Clothing'),
        ('Utilities', 'Utilities'),
        ('Rent', 'Rent'),
        ('Entertainment', 'Entertainment'),
        ('Addictions', 'Addictions'),
        ('Other', 'Other'),
        
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=category_choices)
    date = models.DateField()

    def __str__(self):
        return f'{self.description} - {self.amount}'

    class Meta:
        ordering = ['-date']