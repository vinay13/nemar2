# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_bp_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bp_chart',
            name='Age',
            field=models.CharField(max_length=128),
        ),
    ]
