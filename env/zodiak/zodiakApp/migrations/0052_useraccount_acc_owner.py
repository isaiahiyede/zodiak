# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0051_job_batch_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='acc_owner',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
