# Generated by Django 4.2.7 on 2023-11-18 07:35

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_expense_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_product_image.png', upload_to=app1.models.product_image_filename),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Outside_Food', 'Outside_Food'), ('Clothing', 'Clothing'), ('Utilities', 'Utilities'), ('Rent', 'Rent'), ('Entertainment', 'Entertainment'), ('Addictions', 'Addictions'), ('Other', 'Other')], max_length=20),
        ),
    ]