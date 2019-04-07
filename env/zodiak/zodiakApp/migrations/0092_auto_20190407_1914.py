# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0091_useraccount_cust_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='finances',
            name='job_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='finances',
            name='received',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finances',
            name='date_paid',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
