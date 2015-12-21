# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0023_specialize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='specialize',
            field=models.ForeignKey(to='health.Specialize'),
        ),
    ]
