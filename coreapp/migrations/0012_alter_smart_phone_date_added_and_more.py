# Generated by Django 4.1.1 on 2022-10-18 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0011_alter_smart_phone_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 12, 9, 950365)),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 12, 9, 951365)),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tabs',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 12, 9, 951365)),
        ),
    ]
