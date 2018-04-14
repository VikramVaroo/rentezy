# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-13 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team6', '0047_merge_20180329_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='status',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 13, 19, 52, 34, 603380)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 13, 19, 52, 34, 603400)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 13, 19, 52, 34, 603328)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 13, 19, 52, 34, 603360)),
        ),
    ]
