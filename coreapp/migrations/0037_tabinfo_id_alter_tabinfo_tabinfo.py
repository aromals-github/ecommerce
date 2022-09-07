# Generated by Django 4.1.1 on 2022-09-07 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0036_auto_20220905_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabinfo',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tabinfo',
            name='tabinfo',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, to='coreapp.tabs'),
        ),
    ]
