# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('plant_height', models.IntegerField(default=0)),
                ('plant_image', models.ImageField(upload_to=None)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='plant',
            name='height',
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_text',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='record',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Plant'),
        ),
    ]
