# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 18:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team6', '0058_merge_20180417_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='location',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 17, 18, 56, 38, 797000)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 17, 18, 56, 38, 797000)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 17, 18, 56, 38, 797000)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_time',
            field=models.TimeField(default=datetime.datetime(2018, 4, 17, 18, 56, 38, 797000)),
        ),
    ]
