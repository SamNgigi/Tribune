# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_article_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='post',
            new_name='body',
        ),
    ]
