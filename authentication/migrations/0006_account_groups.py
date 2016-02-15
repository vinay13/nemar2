# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_account_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ForeignKey(blank=True, to='authentication.UserGroup', null=True),
        ),
    ]
