# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0030_healthinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('LivingStandard', models.CharField(default='abc', max_length=128)),
                ('OwnLand', models.CharField(default='abc', max_length=128)),
                ('OwnVechile', models.CharField(default='abc', max_length=128)),
                ('Occupation', models.CharField(default='abc', max_length=128)),
                ('AnnualIncome', models.CharField(default='abc', max_length=128)),
                ('BankAccount', models.CharField(default='abc', max_length=128)),
                ('Loan1', models.CharField(default='abc', max_length=128)),
                ('Loan2', models.CharField(default='abc', max_length=128)),
                ('Loan3', models.CharField(default='abc', max_length=128)),
                ('ssi', models.CharField(default='abc', max_length=128)),
                ('remark', models.CharField(default='abc', max_length=128)),
                ('emailID', models.CharField(default='abc', max_length=128)),
            ],
        ),
    ]
