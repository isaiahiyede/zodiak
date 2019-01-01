# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0018_auto_20190101_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='rm_updated',
            field=models.BooleanField(default=False),
        ),
    ]
