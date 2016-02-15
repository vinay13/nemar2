# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('groupname', models.CharField(default=b'admin', max_length=32)),
                ('priviledges', models.CharField(default=b'socialinfo', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupCustom',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uid', models.CharField(default=b's', max_length=32)),
                ('gid', models.CharField(default=b't', max_length=43)),
                ('customerPrividges', models.CharField(default=b'ty', max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(default=b'a', max_length=28)),
                ('password', models.CharField(default=b'a', max_length=29)),
                ('emailid', models.CharField(default=b'a', max_length=30)),
                ('usergroup', models.CharField(default=b'a', max_length=30)),
                ('status', models.CharField(default=b'a', max_length=29)),
                ('online', models.CharField(default=b'a', max_length=29)),
                ('img', models.CharField(default=b'a', max_length=29)),
                ('mobileno', models.CharField(default=b'a', max_length=29)),
                ('createdate', models.CharField(default=b'a', max_length=29)),
                ('lastdate', models.CharField(default=b'a', max_length=29)),
                ('updatetime', models.CharField(default=b'a', max_length=29)),
                ('sessions', models.CharField(default=b'a', max_length=29)),
                ('loginfailures', models.CharField(default=b'a', max_length=29)),
            ],
        ),
    ]
