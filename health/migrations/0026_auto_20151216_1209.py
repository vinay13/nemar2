# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0025_auto_20151216_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorlist',
            old_name='address',
            new_name='clinic_address',
        ),
        migrations.AddField(
            model_name='doctorlist',
            name='contact_no',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='doctorlist',
            name='home_address',
            field=models.CharField(default='address', max_length=128),
        ),
        migrations.AddField(
            model_name='doctorlist',
            name='hospital_address',
            field=models.CharField(default='address', max_length=128),
        ),
    ]
