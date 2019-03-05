# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0086_auto_20190303_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='finances',
            name='charge_type',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
