# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170115_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='beereal_trainingurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
