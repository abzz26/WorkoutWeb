# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 19:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebAppProject', '0022_auto_20170313_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userliked',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
