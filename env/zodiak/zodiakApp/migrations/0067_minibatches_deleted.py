# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0066_auto_20190217_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='minibatches',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
