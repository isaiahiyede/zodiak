# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0064_auto_20190217_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='no_of_arrival_batches',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
    ]
