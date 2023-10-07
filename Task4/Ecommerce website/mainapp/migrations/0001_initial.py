# Generated by Django 3.2.13 on 2023-06-06 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('message', models.CharField(max_length=5000, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.IntegerField(verbose_name='House No')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('landmark', models.CharField(max_length=100, verbose_name='Landmark')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('pincode', models.IntegerField(verbose_name='Pincode')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
