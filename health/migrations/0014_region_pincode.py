# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0013_auto_20151215_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='pincode',
            field=models.IntegerField(default='234098'),
        ),
    ]
