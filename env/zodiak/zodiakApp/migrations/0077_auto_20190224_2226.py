# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0076_auto_20190224_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finances',
            name='job_finance',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.Job'),
        ),
    ]
