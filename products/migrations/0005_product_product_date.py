# Generated by Django 2.2.8 on 2019-12-23 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191221_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]