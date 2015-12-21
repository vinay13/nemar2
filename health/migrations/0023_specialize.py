# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0022_auto_20151215_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sname', models.CharField(default='null', max_length=128)),
            ],
        ),
    ]
