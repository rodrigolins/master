# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_log_sensor_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
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
