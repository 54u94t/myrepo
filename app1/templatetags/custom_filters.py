from django import template

register = template.Library()

@register.filter(name='total_price')
def total_price(products):
    return sum(item.price for item in products)

@register.filter(name='total_expense')
def total_expense(expenses):
    return sum(item.amount for item in expenses)
