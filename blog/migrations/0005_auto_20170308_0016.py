# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_user_theme_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='theme_scheme',
            field=models.CharField(default='Pisces', help_text='three option: Mist, Muse, Pisces', max_length=64),
        ),
    ]
