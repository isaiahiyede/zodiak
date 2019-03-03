# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0084_job_job_arrival_status_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='containertypes',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documents',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
