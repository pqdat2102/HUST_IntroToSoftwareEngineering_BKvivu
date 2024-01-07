# Generated by Django 4.2.7 on 2024-01-04 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 1, 1, 36, 62327)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 1, 1, 36, 64329)),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 1, 1, 36, 65419)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 1, 1, 36, 63329)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 1, 1, 36, 62327)),
        ),
    ]
