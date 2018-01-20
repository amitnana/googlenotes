# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-03 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0003_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='label',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='mynote.Label'),
        ),
        migrations.AlterField(
            model_name='label',
            name='label',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
