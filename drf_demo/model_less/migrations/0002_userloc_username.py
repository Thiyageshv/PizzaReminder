# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_less', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userloc',
            name='username',
            field=models.CharField(default=b'kabali', max_length=200),
        ),
    ]
