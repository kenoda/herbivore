# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-09 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='plant_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
