# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-06 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_auto_20170425_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='botActived',
            field=models.BooleanField(default=True),
        ),
    ]
