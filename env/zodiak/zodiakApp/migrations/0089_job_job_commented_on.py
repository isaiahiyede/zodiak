# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0088_auto_20190309_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_commented_on',
            field=models.BooleanField(default=False),
        ),
    ]
