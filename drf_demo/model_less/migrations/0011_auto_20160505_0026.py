# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_less', '0010_auto_20160504_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupusers',
            name='users',
            field=models.CharField(max_length=200, null=True),
        ),
    ]