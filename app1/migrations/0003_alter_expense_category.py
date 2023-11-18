# Generated by Django 4.2.7 on 2023-11-18 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Utilities', 'Utilities'), ('Rent', 'Rent'), ('Entertainment', 'Entertainment'), ('Addictions', 'Addictions'), ('Other', 'Other')], max_length=20),
        ),
    ]
