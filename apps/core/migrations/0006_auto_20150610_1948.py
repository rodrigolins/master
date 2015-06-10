# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150610_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensortype',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensortype',
            name='sensor',
            field=models.ManyToManyField(related_name='type', to='core.Sensor'),
        ),
    ]
