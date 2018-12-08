# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0005_auto_20181205_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_amount_balance',
            field=models.FloatField(default=1.0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_amount_paid',
            field=models.FloatField(default=1.0, null=True, blank=True),
        ),
    ]
