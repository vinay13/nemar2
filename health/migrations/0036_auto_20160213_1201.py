# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0035_delete_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('region', models.CharField(default=b'MP', max_length=128)),
                ('parent_id', models.IntegerField(default=b'0')),
                ('region_type', models.CharField(default=b'state', max_length=128, choices=[(b'1', b'states'), (b'2', b'District'), (b'3', b'Zone'), (b'4', b'ward'), (b'5', b'Alley')])),
                ('coordinate', models.CharField(default=b'abc', max_length=128)),
                ('region_order', models.IntegerField(default=1)),
                ('publish', models.IntegerField(default=0)),
                ('pincode', models.IntegerField(default=23409)),
            ],
        ),
        migrations.DeleteModel(
            name='FinancialInfo',
        ),
        migrations.DeleteModel(
            name='HealthInfo',
        ),
        migrations.DeleteModel(
            name='SocialInfo',
        ),
        migrations.RemoveField(
            model_name='specialize',
            name='sname',
        ),
        migrations.AddField(
            model_name='specialize',
            name='name',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='clinic_address',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='home_address',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='hospital_address',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='name',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='meanbloodglucose',
            name='Level',
            field=models.CharField(default=b'High', max_length=128),
        ),
        migrations.AlterField(
            model_name='meanbloodglucose',
            name='Risk',
            field=models.CharField(default=b'Low', max_length=128),
        ),
        migrations.AlterField(
            model_name='meanbloodglucose',
            name='mgDL',
            field=models.CharField(default=b'High', max_length=128),
        ),
        migrations.AlterField(
            model_name='meanbloodglucose',
            name='nmolL',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='meanbloodglucose',
            name='suggested_action',
            field=models.CharField(default=b'Exercise', max_length=128),
        ),
    ]
