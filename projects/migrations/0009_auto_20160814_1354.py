# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 13:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_information_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='photos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=b''), null=True, size=None),
        ),
    ]
