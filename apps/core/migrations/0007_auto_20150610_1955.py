# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150610_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensortype',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensortype',
            name='sensor',
            field=models.ForeignKey(related_name='type', default=1, to='core.Sensor'),
            preserve_default=False,
        ),
    ]
