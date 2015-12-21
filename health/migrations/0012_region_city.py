# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_auto_20151213_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='city',
            field=models.CharField(default='choose', choices=[('rock', 'Rock'), ('jazz/blues', 'Jazz/Blues'), ('blues', 'Blues'), ('r&b', 'R&B'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('hip-hop', 'Hip-Hop')], max_length=1),
        ),
    ]
