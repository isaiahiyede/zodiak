# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0052_useraccount_acc_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='status_of_batch',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='total_batch_cost',
            field=models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='batch',
            name='total_batch_weight',
            field=models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1),
        ),
    ]
