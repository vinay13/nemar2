# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0034_auto_20160204_1234'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Region',
        ),
    ]
