# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='url',
            field=models.URLField(default='http://www.ucdavis.edu'),
            preserve_default=False,
        ),
    ]
