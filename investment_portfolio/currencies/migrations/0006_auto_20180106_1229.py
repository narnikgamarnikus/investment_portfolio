# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-06 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0005_auto_20180106_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name of currency'),
        ),
    ]