# Generated by Django 4.2.7 on 2023-11-20 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_product_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestProduct',
        ),
    ]