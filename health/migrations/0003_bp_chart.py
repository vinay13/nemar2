# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20151210_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='BP_chart',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Age', models.IntegerField(default='18')),
                ('Min', models.IntegerField(default='10')),
                ('Normal', models.IntegerField(default='15')),
                ('Max', models.IntegerField(default='20')),
            ],
        ),
    ]
