# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 10:28
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20161127_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnzlisting',
            name='main_image',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]