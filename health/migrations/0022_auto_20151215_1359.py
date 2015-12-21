# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0021_auto_20151215_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_order',
            field=models.IntegerField(default='1'),
        ),
    ]
