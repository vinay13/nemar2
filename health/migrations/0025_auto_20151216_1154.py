# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0024_auto_20151216_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='region',
            field=models.ForeignKey(to='health.Region'),
        ),
    ]
