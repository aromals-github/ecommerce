# Generated by Django 4.1 on 2022-10-11 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_purchase', '0006_cart_product_smartphones_cart_products_tabs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products_tabs',
            new_name='product_tabs',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='products_watches',
            new_name='product_watches',
        ),
    ]