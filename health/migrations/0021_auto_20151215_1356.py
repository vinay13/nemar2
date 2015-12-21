# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_auto_20151215_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, default='Dr. ')),
                ('address', models.CharField(max_length=128, default='address')),
                ('specialize', models.CharField(max_length=128, default='neurosergeon')),
                ('region', models.CharField(max_length=128, default='MP')),
            ],
        ),
        migrations.AlterField(
            model_name='region',
            name='region_order',
            field=models.IntegerField(max_length=128, default='1'),
        ),
    ]
