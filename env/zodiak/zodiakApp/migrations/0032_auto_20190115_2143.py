# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0031_auto_20190113_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='demurrage_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='demurrage_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
