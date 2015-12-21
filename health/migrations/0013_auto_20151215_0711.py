# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_region_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='city',
            field=models.CharField(max_length=19, choices=[('rock', 'Rock'), ('jazz/blues', 'Jazz/Blues'), ('blues', 'Blues'), ('r&b', 'R&B'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('hip-hop', 'Hip-Hop')], default='choose'),
        ),
    ]
