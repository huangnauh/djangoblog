# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=6, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')])),
                ('telphone', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('mobile', models.CharField(max_length=18, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
