# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='arbit',
        ),
        migrations.RemoveField(
            model_name='table',
            name='title',
        ),
        migrations.AddField(
            model_name='table',
            name='Level',
            field=models.CharField(max_length=128, default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='table',
            name='Risk',
            field=models.CharField(max_length=128, default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='table',
            name='mgDL',
            field=models.CharField(max_length=128, default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='table',
            name='nmolL',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='table',
            name='suggested_action',
            field=models.CharField(max_length=128, default='SOME STRING'),
        ),
    ]
