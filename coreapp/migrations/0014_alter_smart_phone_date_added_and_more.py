# Generated by Django 4.1 on 2022-09-25 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0013_smartphoneinfo_delete_brands_delete_smart_phoneinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 11, 1, 9, 939674)),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 11, 1, 9, 939674)),
        ),
        migrations.AlterField(
            model_name='tabs',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 11, 1, 9, 939674)),
        ),
    ]
