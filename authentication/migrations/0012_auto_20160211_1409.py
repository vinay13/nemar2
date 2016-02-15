# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20160211_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.IntegerField(default=0),
        ),
    ]
