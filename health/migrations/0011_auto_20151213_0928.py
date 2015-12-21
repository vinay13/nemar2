# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_auto_20151212_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C201to210',
            field=models.CharField(default='high', max_length=128),
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C211to220',
            field=models.CharField(default='high', max_length=128),
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C221to230',
            field=models.CharField(default='high', max_length=128),
        ),
    ]
