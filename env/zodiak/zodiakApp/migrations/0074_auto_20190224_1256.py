# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0073_auto_20190223_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_arr_stat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_details',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_documentation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_finances',
            field=models.BooleanField(default=False),
        ),
    ]
