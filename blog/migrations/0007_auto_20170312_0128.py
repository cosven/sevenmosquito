# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='site_desc',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='site_subtitle',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='site_title',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='theme_scheme',
            field=models.CharField(choices=[('Mist', 'mist'), ('Muse', 'muse'), ('Pisces', 'pisces')], default='Pisces', max_length=64),
        ),
    ]
