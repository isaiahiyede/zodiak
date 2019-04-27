# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='doc_time',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='finances',
            name='time_paid',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statusrec',
            name='stat_time',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
