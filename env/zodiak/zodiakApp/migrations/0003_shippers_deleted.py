# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0002_auto_20190427_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippers',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
