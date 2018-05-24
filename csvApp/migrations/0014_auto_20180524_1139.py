# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0013_auto_20180524_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]