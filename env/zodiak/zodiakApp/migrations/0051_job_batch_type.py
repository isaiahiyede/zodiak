# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0050_auto_20190203_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='batch_type',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.Batch'),
        ),
    ]
