# Generated by Django 4.1 on 2022-09-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='images',
            field=models.FileField(blank=True, upload_to='phone_image'),
        ),
    ]