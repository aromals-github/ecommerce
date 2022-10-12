# Generated by Django 4.1 on 2022-10-12 05:10

import datetime
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smart_phone',
            fields=[
                ('phone_id', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('colour', models.CharField(max_length=10, null=True)),
                ('images', models.ImageField(blank=True, upload_to='phone_image')),
                ('storage', models.IntegerField(default=128, validators=[django.core.validators.MaxValueValidator(512), django.core.validators.MinValueValidator(128)])),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('instock', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('operating_system', models.CharField(max_length=30, null=True)),
                ('camera', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 10, 12, 10, 40, 22, 960238))),
                ('ram', models.IntegerField(blank=True, default=4, null=True)),
            ],
            options={
                'verbose_name_plural': 'Smart Phones',
            },
        ),
        migrations.CreateModel(
            name='Smart_watch',
            fields=[
                ('watch_id', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=10, null=True)),
                ('images', models.ImageField(blank=True, upload_to='watch_image')),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('instock', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 10, 12, 10, 40, 22, 975865))),
            ],
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('tab_id', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=10, null=True)),
                ('images', models.FileField(upload_to='tablet_image')),
                ('display_size', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, null=True)),
                ('instock', models.IntegerField(null=True)),
                ('storage', models.IntegerField(default=128, validators=[django.core.validators.MinValueValidator(128), django.core.validators.MaxValueValidator(1024)])),
                ('description', models.CharField(max_length=1000, null=True)),
                ('ram', models.IntegerField(blank=True, default=4, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 10, 12, 10, 40, 22, 975865))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
