# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0061_auto_20190217_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='paar_date',
        ),
        migrations.AddField(
            model_name='job',
            name='paar2_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
