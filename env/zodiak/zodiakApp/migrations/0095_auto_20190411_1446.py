# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0094_finances_time_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finances',
            name='time_paid',
        ),
        migrations.AlterField(
            model_name='finances',
            name='date_paid',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
