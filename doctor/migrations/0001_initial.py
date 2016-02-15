# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=128, default='Dr. ')),
                ('specialize', models.CharField(max_length=128, default='s')),
                ('experience', models.CharField(max_length=12, default='2')),
                ('region', models.CharField(max_length=128, default='JBP')),
                ('contact_no', models.IntegerField(default='+91')),
                ('home_address', models.TextField()),
                ('hospital_address', models.TextField()),
                ('clinic_address', models.TextField()),
            ],
        ),
    ]
