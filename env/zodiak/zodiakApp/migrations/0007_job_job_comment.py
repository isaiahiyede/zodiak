# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0006_auto_20181207_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_comment',
            field=models.TextField(null=True, blank=True),
        ),
    ]
