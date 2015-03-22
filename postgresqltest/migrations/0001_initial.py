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
                ('street_address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=2)),
                ('zipe', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_name', models.CharField(max_length=80)),
                ('shipping_address', models.ForeignKey(to='postgresqltest.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
