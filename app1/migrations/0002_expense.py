# Generated by Django 4.2.7 on 2023-11-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Groceries', 'Groceries'), ('Utilities', 'Utilities'), ('Rent', 'Rent'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=20)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]