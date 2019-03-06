# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0087_auto_20190305_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_new_comment',
            field=models.BooleanField(default=False),
        ),
    ]
