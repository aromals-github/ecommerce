# Generated by Django 4.1 on 2022-08-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0006_rename_smart_watche_smart_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smart_phone',
            name='id',
        ),
        migrations.AlterField(
            model_name='smart_phone',
            name='phone_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
