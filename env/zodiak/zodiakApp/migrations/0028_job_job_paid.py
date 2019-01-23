# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0027_auto_20190106_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_paid',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
