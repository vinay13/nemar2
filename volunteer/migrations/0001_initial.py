# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=33, default='MP')),
                ('city', models.CharField(max_length=21, default='JBP')),
                ('zone', models.CharField(max_length=23, default='napier town')),
                ('address', models.CharField(max_length=127, default='23 Ranjhi Market')),
                ('contactno', models.IntegerField(default='+91')),
                ('alt_contactno', models.IntegerField(default='+91')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=123, default='x')),
                ('school_yearofpassing', models.CharField(max_length=124, default='y')),
                ('graduation', models.CharField(max_length=12, default='Yes')),
                ('college_name', models.CharField(max_length=124, default='o')),
                ('grad_yearofpassing', models.CharField(max_length=123, default='z')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=128, default='firstname')),
                ('lname', models.CharField(max_length=128, default='lastname')),
                ('DOB', models.CharField(max_length=128, default='10-10-2010')),
                ('gender', models.CharField(max_length=128, default='M')),
                ('Hostpital_name', models.CharField(max_length=128, default='q')),
                ('Doctor_name', models.CharField(max_length=128, default='Dr.')),
                ('ownLaptop', models.CharField(max_length=128, default='yes')),
                ('ownVechile', models.CharField(max_length=128, default='yes')),
            ],
        ),
    ]
