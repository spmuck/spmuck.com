# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
    ]
