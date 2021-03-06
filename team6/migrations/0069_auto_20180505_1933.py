# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-05 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team6', '0068_merge_20180502_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_owner',
            name='license',
            field=models.FileField(default=b'', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.DateField(default=datetime.datetime(2018, 5, 5, 19, 33, 42, 185128)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_date',
            field=models.DateField(default=b'2018-05-05 19:33:42.184178'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='drop_time',
            field=models.TimeField(default=datetime.datetime(2018, 5, 5, 19, 33, 42, 184202)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 5, 19, 33, 42, 184123)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_time',
            field=models.TimeField(default=datetime.datetime(2018, 5, 5, 19, 33, 42, 184158)),
        ),
    ]
