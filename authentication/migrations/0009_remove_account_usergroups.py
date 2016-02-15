# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_account_usergroups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='usergroups',
        ),
    ]
