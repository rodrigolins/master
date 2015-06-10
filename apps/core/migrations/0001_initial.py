# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('value', models.FloatField()),
                ('unity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('unity', models.CharField(max_length=10)),
                ('boundary', models.CharField(max_length=2, choices=[(b'eq', b'Equals'), (b'gt', b'Grater than'), (b'lt', b'Less than')])),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sensor_model', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('min_value', models.FloatField()),
                ('max_value', models.FloatField()),
            ],
        ),
    ]
