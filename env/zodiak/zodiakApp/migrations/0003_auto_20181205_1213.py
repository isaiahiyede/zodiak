# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0002_job_job_paid_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_shipper',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
