# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-09 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170704_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
    ]
