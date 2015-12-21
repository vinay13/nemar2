# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0029_socialinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allergy', models.CharField(max_length=128, default='abc')),
                ('PhysicalChallenged', models.CharField(max_length=128, default='abc')),
                ('BloodGroup', models.CharField(max_length=128, default='abc')),
                ('HomeAddress', models.CharField(max_length=128, default='abc')),
                ('OfficeAddress', models.CharField(max_length=128, default='abc')),
                ('ChronicDisease1', models.CharField(max_length=128, default='abc')),
                ('ChronicDisease2', models.CharField(max_length=128, default='abc')),
                ('ChronicDisease3', models.CharField(max_length=128, default='abc')),
                ('TroubleDisease1', models.CharField(max_length=128, default='abc')),
                ('TroubleDisease2', models.CharField(max_length=128, default='abc')),
                ('TroubleDisease3', models.CharField(max_length=128, default='abc')),
                ('Digestion', models.CharField(max_length=128, default='abc')),
                ('Diagnosed', models.CharField(max_length=128, default='abc')),
                ('Preference', models.CharField(max_length=128, default='abc')),
            ],
        ),
    ]
