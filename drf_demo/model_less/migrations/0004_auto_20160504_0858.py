# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_less', '0003_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='group',
            new_name='groupusers',
        ),
    ]