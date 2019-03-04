# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0077_auto_20190224_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='customer_type',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='ref_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
