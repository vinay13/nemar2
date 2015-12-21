# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meanbloodg',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Level', models.CharField(default='SOME STRING', max_length=128)),
                ('mgDL', models.CharField(default='SOME STRING', max_length=128)),
                ('nmolL', models.IntegerField(default='1')),
                ('Risk', models.CharField(default='SOME STRING', max_length=128)),
                ('suggested_action', models.CharField(default='SOME STRING', max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
