# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0016_region_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='region_name',
        ),
        migrations.RemoveField(
            model_name='region',
            name='region_type',
        ),
    ]
