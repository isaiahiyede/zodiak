# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0088_auto_20190303_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='staff_account',
            field=models.BooleanField(default=True),
        ),
    ]
