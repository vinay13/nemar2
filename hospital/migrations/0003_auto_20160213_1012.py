# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20160104_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='BloodTest',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='CTSCAN',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='ICU',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='IICU',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='IPD',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='MRI',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='OPD',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='XRAY',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contactno',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='fullname',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
