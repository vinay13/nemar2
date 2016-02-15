# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20160206_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialinfo',
            name='birthplace',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='children',
            field=models.IntegerField(default=b'ds'),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='delivery',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='domicile',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='fathername',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='fcontactno',
            field=models.IntegerField(default=b'ds'),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='fdob',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='gender',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='girlCount',
            field=models.IntegerField(default=b'ds'),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='marriagedate',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='mcontactno',
            field=models.IntegerField(default=b'ds'),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='mdob',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='mothername',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='sDOB',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='siblings',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='spouseName',
            field=models.CharField(default=b'ds', max_length=128),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='yearofliving',
            field=models.CharField(default=b'ds', max_length=128),
        ),
    ]
