# Generated by Django 4.1 on 2022-08-25 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0015_tabs_storage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smart_phone',
            name='availablity',
        ),
        migrations.RemoveField(
            model_name='smart_watch',
            name='availablity',
        ),
        migrations.RemoveField(
            model_name='tabs',
            name='availablity',
        ),
    ]