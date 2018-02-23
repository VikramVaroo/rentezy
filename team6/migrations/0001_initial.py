# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 22:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelNumber', models.CharField(max_length=200)),
                ('modelName', models.CharField(max_length=200)),
                ('regNumber', models.CharField(max_length=200)),
                ('insNumber', models.CharField(max_length=200)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerId', models.IntegerField()),
                ('firstName', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
