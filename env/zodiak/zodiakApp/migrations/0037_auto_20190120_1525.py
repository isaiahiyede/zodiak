# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0036_auto_20190119_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='airline_tracking_number',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='carrier_agent_acct_no',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
