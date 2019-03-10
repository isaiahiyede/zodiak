# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0086_auto_20190306_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_date_of_arrival',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_end_date',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_start_date',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
