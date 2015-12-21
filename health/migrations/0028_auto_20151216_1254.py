# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0027_medicaloperate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaloperate',
            name='operate_type',
            field=models.CharField(choices=[('expertise', 'Expertise'), ('disease', 'Disease'), ('symptoms', 'Symptoms')], default='xyz', max_length=128),
        ),
    ]
