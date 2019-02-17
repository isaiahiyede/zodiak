# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0059_job_job_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='minibatches',
            name='carrier_name',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minibatches',
            name='no_of_containers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minibatches',
            name='type_of_container',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
