# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20160114_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.Category'),
        ),
    ]
