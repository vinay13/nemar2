# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_account_usergroups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='account',
            name='group',
            field=models.IntegerField(default=0),
        ),
    ]
