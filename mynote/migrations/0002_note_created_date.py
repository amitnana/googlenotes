# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-01 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
