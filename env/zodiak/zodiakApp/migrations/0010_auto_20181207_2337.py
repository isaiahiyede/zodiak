# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0009_auto_20181207_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
