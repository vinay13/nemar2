# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0017_auto_20151215_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='city',
        ),
        migrations.RemoveField(
            model_name='region',
            name='state',
        ),
        migrations.AddField(
            model_name='region',
            name='region',
            field=models.CharField(default='MP', max_length=128),
        ),
        migrations.AddField(
            model_name='region',
            name='region_type',
            field=models.CharField(default='state', max_length=128),
        ),
    ]
