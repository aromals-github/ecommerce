# Generated by Django 4.1 on 2022-09-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0030_auto_20220902_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneinfo',
            name='display',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='phoneinfo',
            name='ram',
            field=models.IntegerField(default=2, null=True),
        ),
    ]
