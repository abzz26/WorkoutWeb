# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppProject', '0017_auto_20170308_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
