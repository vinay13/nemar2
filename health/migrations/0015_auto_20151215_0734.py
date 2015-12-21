# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0014_region_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='city',
            field=models.CharField(max_length=19, default='choose', choices=[('rock', 'Jabalpur'), ('jazz/blues', 'Bhopal'), ('blues', 'Itarsi'), ('r&b', 'Indore'), ('jazz', 'Allahabad'), ('pop', 'Lucknow'), ('hip-hop', 'Varanasi')]),
        ),
    ]
