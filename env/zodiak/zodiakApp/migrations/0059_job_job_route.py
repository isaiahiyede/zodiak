# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0058_job_no_of_arrival_batches'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_route',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
