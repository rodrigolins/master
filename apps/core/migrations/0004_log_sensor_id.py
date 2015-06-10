# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sensortype'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='sensor_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
