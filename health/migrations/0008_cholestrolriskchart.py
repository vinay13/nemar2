# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_auto_20151211_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cholestrolriskchart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Age', models.CharField(default='21', max_length=128)),
                ('greaterthan150', models.CharField(default='High', max_length=128)),
            ],
        ),
    ]
