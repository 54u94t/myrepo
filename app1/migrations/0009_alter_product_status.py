# Generated by Django 4.2.7 on 2023-11-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('acquired', 'Acquired'), ('classified', 'Classified'), ('on sale', 'On Sale'), ('sold', 'Sold')], default='acquired', max_length=20),
        ),
    ]
