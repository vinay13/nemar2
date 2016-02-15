# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0033_region_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorlist',
            name='region',
        ),
        migrations.RemoveField(
            model_name='doctorlist',
            name='specialize',
        ),
        migrations.RemoveField(
            model_name='region',
            name='city',
        ),
    ]
