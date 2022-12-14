# Generated by Django 4.1.1 on 2022-10-18 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0011_alter_smart_phone_date_added_and_more'),
        ('customer_purchase', '0012_orderitem_product_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_tab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.tabs'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.smart_phone'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_watch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.smart_watch'),
        ),
    ]
