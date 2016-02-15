# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0036_auto_20160213_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
