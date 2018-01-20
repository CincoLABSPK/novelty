# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_survey_submit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
