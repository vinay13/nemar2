# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_usergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='groups',
            field=models.ForeignKey(blank=True, to='authentication.UserGroup', null=True),
        ),
    ]
