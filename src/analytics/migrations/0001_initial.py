# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0005_auto_20170915_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestap', models.DateTimeField(auto_now_add=True)),
                ('kirr_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.KirrUrl')),
            ],
        ),
    ]
