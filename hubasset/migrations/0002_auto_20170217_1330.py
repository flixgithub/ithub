# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-17 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubasset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetbj',
            name='asset_id',
            field=models.CharField(db_column='ASSET_ID', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetbj',
            name='hostname',
            field=models.CharField(db_column='HOSTNAME', db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='assetbj',
            name='ilom_ip',
            field=models.CharField(db_column='ILOM_IP', db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='assetnj',
            name='asset_id',
            field=models.CharField(db_column='ASSET_ID', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetnj',
            name='hostname',
            field=models.CharField(db_column='HOSTNAME', db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='assetnj',
            name='ilom_ip',
            field=models.CharField(db_column='ILOM_IP', db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='assetsh',
            name='asset_id',
            field=models.CharField(db_column='ASSET_ID', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetsh',
            name='hostname',
            field=models.CharField(db_column='HOSTNAME', db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='assetsh',
            name='ilom_ip',
            field=models.CharField(db_column='ILOM_IP', db_index=True, max_length=50),
        ),
    ]
