# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0032_auto_20151228_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='city',
            field=models.CharField(default=b'choose', max_length=19),
        ),
    ]
