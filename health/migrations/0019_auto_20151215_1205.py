# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0018_auto_20151215_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_type',
            field=models.CharField(default='state', max_length=128, choices=[('1', 'states'), ('2', 'District'), ('3', 'Zone'), ('4', 'ward'), ('5', 'Alley')]),
        ),
    ]
