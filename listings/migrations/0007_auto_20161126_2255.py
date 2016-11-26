# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20161126_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='TNZRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField()),
                ('o_id', models.IntegerField()),
                ('label', models.CharField(max_length=200)),
                ('name_key', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='tnztag',
            name='name_key',
            field=models.CharField(max_length=200),
        ),
    ]