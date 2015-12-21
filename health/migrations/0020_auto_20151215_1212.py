# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0019_auto_20151215_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_order',
            field=models.CharField(default='MP', max_length=128, choices=[('1', 'MP'), ('2', 'UP'), ('3', 'GUJRAT'), ('4', 'Orissa'), ('5', 'Punjab')]),
        ),
    ]
