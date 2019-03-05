# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0087_finances_charge_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minibatches',
            name='no_of_containers',
        ),
        migrations.RemoveField(
            model_name='minibatches',
            name='type_of_container',
        ),
        migrations.AddField(
            model_name='minibatches',
            name='job_description',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
