# Generated by Django 4.1 on 2022-08-24 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_tabs_alter_smart_phone_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smart_watch',
            name='brand',
        ),
    ]