# Generated by Django 4.1 on 2022-09-23 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0008_alter_smart_phone_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 10, 44, 41, 478782)),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 10, 44, 41, 478782)),
        ),
        migrations.AlterField(
            model_name='tabs',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 10, 44, 41, 478782)),
        ),
    ]
