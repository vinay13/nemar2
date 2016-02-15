# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
        migrations.CreateModel(
            name='HealthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('Allergy', models.CharField(default='abc', max_length=128)),
                ('PhysicalChallenged', models.CharField(default='abc', max_length=128)),
                ('BloodGroup', models.CharField(default='abc', max_length=128)),
                ('HomeAddress', models.CharField(default='abc', max_length=128)),
                ('OfficeAddress', models.CharField(default='abc', max_length=128)),
                ('ChronicDisease1', models.CharField(default='abc', max_length=128)),
                ('ChronicDisease2', models.CharField(default='abc', max_length=128)),
                ('ChronicDisease3', models.CharField(default='abc', max_length=128)),
                ('TroubleDisease1', models.CharField(default='abc', max_length=128)),
                ('TroubleDisease2', models.CharField(default='abc', max_length=128)),
                ('TroubleDisease3', models.CharField(default='abc', max_length=128)),
                ('Digestion', models.CharField(default='abc', max_length=128)),
                ('Diagnosed', models.CharField(default='abc', max_length=128)),
                ('Preference', models.CharField(default='abc', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('siblings', models.CharField(default=' ', max_length=128)),
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
