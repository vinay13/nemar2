# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_cholestrolriskchart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C151to159',
            field=models.CharField(default='Low', max_length=128),
        ),
    ]
