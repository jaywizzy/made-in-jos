# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-28 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='categories_images'),
        ),
    ]
