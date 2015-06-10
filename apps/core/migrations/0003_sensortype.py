# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_property_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sensor', models.ManyToManyField(to='core.Sensor')),
            ],
        ),
    ]
