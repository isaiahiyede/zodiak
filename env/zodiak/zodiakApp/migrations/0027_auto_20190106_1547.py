# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0026_status_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='alias',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
