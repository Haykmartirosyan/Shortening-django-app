# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20170915_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]