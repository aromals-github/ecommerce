# Generated by Django 4.1.1 on 2022-09-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0038_alter_smart_phone_name_alter_tabinfo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabs',
            name='name',
            field=models.CharField(max_length=30, verbose_name=str),
        ),
    ]