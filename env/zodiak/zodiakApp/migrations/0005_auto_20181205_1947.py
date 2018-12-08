# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0004_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_cost',
            field=models.FloatField(default=1.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
