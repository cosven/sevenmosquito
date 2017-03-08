# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170305_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='theme_scheme',
            field=models.CharField(default=b'Pisces', help_text=b'three option: Mist, Muse, Pisces', max_length=64),
        ),
    ]
