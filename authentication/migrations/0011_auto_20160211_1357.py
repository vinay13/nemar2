# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20160211_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.ForeignKey(blank=True, to='authentication.UserGroup', null=True),
        ),
    ]
