# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150610_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensortype',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_type',
            field=models.ForeignKey(related_name='+', default=1, to='core.SensorType'),
            preserve_default=False,
        ),
    ]
