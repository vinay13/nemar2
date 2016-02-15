# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialinfo',
            old_name='BirthPlace',
            new_name='birthplace',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Children',
            new_name='children',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='ContactNo',
            new_name='contactno',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Delivery',
            new_name='delivery',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Dob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Domicile',
            new_name='domicile',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='FatherName',
            new_name='fathername',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='GirlCount',
            new_name='fcontactno',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='Gender',
            new_name='fdob',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='FirstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='MarriageDate',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='fContactNo',
            new_name='girlCount',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='LastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='MotherName',
            new_name='marriagedate',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='mContactNo',
            new_name='mcontactno',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='SpouseName',
            new_name='mdob',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='YearOfLiving',
            new_name='mothername',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='fDOB',
            new_name='spouseName',
        ),
        migrations.RenameField(
            model_name='socialinfo',
            old_name='mDOB',
            new_name='yearofliving',
        ),
    ]
