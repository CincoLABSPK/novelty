# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-03 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0028_auto_20180124_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyresponse',
            old_name='username',
            new_name='email',
        ),
    ]
