# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('workers', '0001_initial'), ('workers', '0002_auto_20170413_1845'), ('workers', '0003_auto_20170414_0924'), ('workers', '0004_auto_20170414_0930')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Programmer', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='jobposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.JobPosition'),
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='jobposition',
        ),
        migrations.AddField(
            model_name='employee',
            name='is_working',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='jobposition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.JobPosition'),
        ),
    ]
