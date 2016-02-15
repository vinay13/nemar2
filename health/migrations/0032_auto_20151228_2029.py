# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0031_financialinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Siblings',
            new_name='siblings',
        ),
    ]
