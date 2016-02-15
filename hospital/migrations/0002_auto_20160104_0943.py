# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='BloodTest',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=18),
        ),
        migrations.AddField(
            model_name='hospital',
            name='CTSCAN',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AddField(
            model_name='hospital',
            name='ICU',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AddField(
            model_name='hospital',
            name='IICU',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AddField(
            model_name='hospital',
            name='IPD',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AddField(
            model_name='hospital',
            name='MRI',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AddField(
            model_name='hospital',
            name='XRAY',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=28),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='OPD',
            field=models.CharField(default='Choose', choices=[('1', 'Yes'), ('2', 'No')], max_length=29),
        ),
    ]
