# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_auto_20170414_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobposition', to='workers.JobPosition'),
        ),
    ]
