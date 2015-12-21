# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0015_auto_20151215_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='state',
            field=models.CharField(default='choose', max_length=19, choices=[('rock', 'MP'), ('jazz/blues', 'UP'), ('blues', 'Gujrat'), ('r&b', 'Maharastra'), ('jazz', 'Andhra Pradesh'), ('pop', 'West Bengal'), ('hip-hop', 'Bihar')]),
        ),
    ]
