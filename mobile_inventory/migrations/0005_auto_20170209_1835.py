# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_inventory', '0004_auto_20170209_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='service_tag',
            field=models.CharField(max_length=100, verbose_name='Service Tag'),
        ),
    ]
