# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_less', '0008_auto_20160504_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupusers',
            name='users',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
