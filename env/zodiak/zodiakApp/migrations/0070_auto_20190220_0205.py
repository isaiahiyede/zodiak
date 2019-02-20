# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0069_job_job_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finances',
            name='other_charges_due_carrier',
            field=models.FloatField(blank=True, null=True, default=0.0),
        ),
    ]
