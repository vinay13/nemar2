# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0028_auto_20151216_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(default='abc', max_length=128)),
                ('LastName', models.CharField(default='s', max_length=128)),
                ('Dob', models.CharField(default='ds', max_length=128)),
                ('ContactNo', models.IntegerField(default='1')),
                ('FatherName', models.CharField(default=' ', max_length=128)),
                ('fDOB', models.CharField(default=' ', max_length=128)),
                ('fContactNo', models.IntegerField(default=' ')),
                ('MotherName', models.CharField(default=' ', max_length=128)),
                ('mDOB', models.CharField(default=' ', max_length=128)),
                ('mContactNo', models.IntegerField(default=' ')),
                ('Gender', models.CharField(default=' ', max_length=128)),
                ('Siblings', models.CharField(default=' ', max_length=128)),
                ('SpouseName', models.CharField(default=' ', max_length=128)),
                ('sDOB', models.CharField(default=' ', max_length=128)),
                ('MarriageDate', models.CharField(default=' ', max_length=128)),
                ('Children', models.IntegerField(default=' ')),
                ('GirlCount', models.IntegerField(default=' ')),
                ('BirthPlace', models.CharField(default=' ', max_length=128)),
                ('Delivery', models.CharField(default=' ', max_length=128)),
                ('Domicile', models.CharField(default=' ', max_length=128)),
                ('YearOfLiving', models.CharField(default=' ', max_length=128)),
            ],
        ),
    ]
