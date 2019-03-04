# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0083_auto_20190302_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_arrival_status_mode',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
