# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0026_auto_20151216_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalOperate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operate_name', models.CharField(default='abc', max_length=128)),
                ('operate_type', models.CharField(default='xyz', choices=[('1', 'Expertise'), ('2', 'Disease'), ('3', 'Symptoms')], max_length='128')),
            ],
        ),
    ]
