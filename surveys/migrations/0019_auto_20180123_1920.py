# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-23 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0018_auto_20180123_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='optionorder',
            old_name='option_id',
            new_name='option',
        ),
        migrations.RenameField(
            model_name='optionorder',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questionorder',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questionorder',
            old_name='survey_id',
            new_name='survey',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='survey_response_id',
            new_name='survey_response',
        ),
        migrations.RenameField(
            model_name='surveyresponse',
            old_name='survey_id',
            new_name='survey',
        ),
    ]
