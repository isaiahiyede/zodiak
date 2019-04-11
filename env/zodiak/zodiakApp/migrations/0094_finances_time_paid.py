# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0093_auto_20190407_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='finances',
            name='time_paid',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
