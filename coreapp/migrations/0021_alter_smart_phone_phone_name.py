# Generated by Django 4.1 on 2022-09-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0020_alter_smart_phone_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='phone_name',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
