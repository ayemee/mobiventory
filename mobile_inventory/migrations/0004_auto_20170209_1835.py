# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_inventory', '0003_auto_20170207_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='service_tag',
        ),
        migrations.AddField(
            model_name='device',
            name='service_tag',
            field=models.CharField(default='Hi', max_length=100, verbose_name='Service Tag'),
        ),
    ]
