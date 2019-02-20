# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0057_minibatches'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='no_of_arrival_batches',
            field=models.FloatField(blank=True, null=True, default=0),
        ),
    ]
