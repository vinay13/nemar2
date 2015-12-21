# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_auto_20151211_0901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BP_chart',
            new_name='Bloodpressurechart',
        ),
        migrations.RenameModel(
            old_name='Meanbloodg',
            new_name='Meanbloodglucose',
        ),
    ]
