# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.SmallIntegerField()),
                ('first_name', models.CharField(blank=True, default='', max_length=40)),
                ('last_name', models.CharField(blank=True, default='', max_length=40)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
