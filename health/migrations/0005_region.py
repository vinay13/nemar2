# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_auto_20151211_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('region_name', models.CharField(max_length=128, default='MP')),
                ('parent_id', models.IntegerField(default='0')),
                ('region_type', models.CharField(max_length=128, default='state')),
                ('coordinate', models.CharField(max_length=128, default='abc')),
                ('region_order', models.IntegerField(default='1')),
                ('publish', models.IntegerField(default='0')),
            ],
        ),
    ]
