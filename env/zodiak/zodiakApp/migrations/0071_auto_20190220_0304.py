# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0070_auto_20190220_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finances',
            name='job_finance',
            field=models.OneToOneField(blank=True, null=True, to='zodiakApp.Job'),
        ),
    ]
