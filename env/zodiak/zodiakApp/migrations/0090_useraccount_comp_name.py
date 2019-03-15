# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0089_job_job_commented_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='comp_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
