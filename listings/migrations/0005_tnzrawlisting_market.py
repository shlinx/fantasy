# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20161126_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='tnzrawlisting',
            name='market',
            field=models.CharField(default='en', max_length=5),
            preserve_default=False,
        ),
    ]