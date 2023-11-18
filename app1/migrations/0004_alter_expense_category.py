# Generated by Django 4.2.7 on 2023-11-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Clothing', 'Clothing'), ('Utilities', 'Utilities'), ('Rent', 'Rent'), ('Entertainment', 'Entertainment'), ('Addictions', 'Addictions'), ('Other', 'Other')], max_length=20),
        ),
    ]
