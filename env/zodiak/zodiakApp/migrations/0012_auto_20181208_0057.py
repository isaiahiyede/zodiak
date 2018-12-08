# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0011_auto_20181207_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_date_of_arrival',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
