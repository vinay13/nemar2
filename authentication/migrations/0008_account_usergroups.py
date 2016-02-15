# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20160210_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='usergroups',
            field=models.CharField(default=b'patient', max_length=128, choices=[(b'1', b'patient'), (b'2', b'doctor'), (b'3', b'volunteer'), (b'4', b'admin')]),
        ),
    ]
