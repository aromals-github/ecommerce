# Generated by Django 4.1 on 2022-10-11 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0035_alter_smart_phone_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 20, 54, 1, 460274)),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 20, 54, 1, 460274)),
        ),
        migrations.AlterField(
            model_name='tabs',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 20, 54, 1, 460274)),
        ),
    ]
