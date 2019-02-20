# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0068_auto_20190220_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_paid',
            field=models.BooleanField(default=False),
        ),
    ]
