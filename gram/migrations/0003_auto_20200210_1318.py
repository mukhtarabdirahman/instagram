# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-10 10:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_auto_20200210_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-upload_date']},
        ),
    ]
