# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 11:38
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20180227_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
