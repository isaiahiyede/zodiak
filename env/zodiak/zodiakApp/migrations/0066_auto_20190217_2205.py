# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0065_job_no_of_arrival_batches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_cost',
            field=models.FloatField(blank=True, null=True, default=0.0),
        ),
    ]
