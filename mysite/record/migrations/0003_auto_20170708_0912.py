# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20170708_0356'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='Post',
        ),
        migrations.AlterField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
