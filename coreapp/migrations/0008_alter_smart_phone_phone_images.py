# Generated by Django 4.1 on 2022-08-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0007_remove_smart_phone_id_alter_smart_phone_phone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart_phone',
            name='phone_images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]