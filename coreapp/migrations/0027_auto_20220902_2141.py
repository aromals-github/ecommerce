# Generated by Django 3.2.14 on 2022-09-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0026_smart_phone_phone_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='smart_watch',
            name='watch_id',
            field=models.CharField(default='a', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='smart_phone',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='smart_phone',
            name='phone_id',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]