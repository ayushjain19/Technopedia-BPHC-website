# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
