# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_paid_for',
            field=models.BooleanField(default=False),
        ),
    ]
