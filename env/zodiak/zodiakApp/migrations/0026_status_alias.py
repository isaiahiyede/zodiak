# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0025_auto_20190106_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='alias',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
