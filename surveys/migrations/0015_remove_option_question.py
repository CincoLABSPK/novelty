# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-22 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0014_optionorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
    ]
