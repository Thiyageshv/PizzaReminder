# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 23:35
from __future__ import unicode_literals

from django.db import migrations
import drf_demo.model_less.models


class Migration(migrations.Migration):

    dependencies = [
        ('model_less', '0009_auto_20160504_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupusers',
            name='users',
            field=drf_demo.model_less.models.ListField(default=[0, 0, 0]),
            preserve_default=False,
        ),
    ]
