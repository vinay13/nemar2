# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_cholestrolriskchart_c151to159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cholestrolriskchart',
            old_name='greaterthan150',
            new_name='C150',
        ),
        migrations.RenameField(
            model_name='cholestrolriskchart',
            old_name='C151to159',
            new_name='C151to160',
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C161to170',
            field=models.CharField(default='Low', max_length=128),
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C171to180',
            field=models.CharField(default='Low', max_length=128),
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C181to190',
            field=models.CharField(default='Low', max_length=128),
        ),
        migrations.AddField(
            model_name='cholestrolriskchart',
            name='C191to200',
            field=models.CharField(default='high', max_length=128),
        ),
    ]
