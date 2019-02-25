# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0074_auto_20190224_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_descript',
            field=models.BooleanField(default=False),
        ),
    ]
