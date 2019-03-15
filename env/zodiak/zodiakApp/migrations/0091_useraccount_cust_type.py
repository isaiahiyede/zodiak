# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0090_useraccount_comp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='cust_type',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
