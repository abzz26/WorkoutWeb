# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppProject', '0019_remove_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
