# Generated by Django 4.1 on 2022-10-13 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_alter_smart_phone_date_added_and_more'),
        ('customer_purchase', '0005_remove_cart_products_cart_total_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproducts',
            name='products_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartproducts', to='coreapp.smart_phone'),
        ),
    ]
