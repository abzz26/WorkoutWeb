# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppProject', '0031_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Guest', max_length=128),
        ),
    ]