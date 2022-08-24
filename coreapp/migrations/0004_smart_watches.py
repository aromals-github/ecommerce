# Generated by Django 4.1 on 2022-08-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_smart_phone_avalablity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smart_watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('watch_colour', models.CharField(max_length=10, null=True)),
                ('watch_images', models.ImageField(blank=True, upload_to='watch_image')),
                ('size', models.IntegerField()),
                ('avalablity', models.BooleanField(default=True)),
            ],
        ),
    ]