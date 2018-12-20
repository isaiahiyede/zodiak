# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0014_auto_20181219_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='inputter',
            field=models.BooleanField(default=True),
        ),
    ]
