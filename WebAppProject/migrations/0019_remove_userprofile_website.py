# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppProject', '0018_auto_20170308_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
