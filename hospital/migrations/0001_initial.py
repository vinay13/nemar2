# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(default='h', max_length=128)),
                ('address', models.TextField()),
                ('contactno', models.CharField(default='s', max_length=128)),
                ('OPD', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=128, default='Choose')),
            ],
        ),
    ]
