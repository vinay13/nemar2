# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20160209_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='groups',
        ),
    ]
