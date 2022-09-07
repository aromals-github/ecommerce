# Generated by Django 4.1.1 on 2022-09-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0041_remove_tabinfo_tabinfo_remove_watchinfo_watchinfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='smart_phone',
            name='camera',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='smart_phone',
            name='operating_system',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
