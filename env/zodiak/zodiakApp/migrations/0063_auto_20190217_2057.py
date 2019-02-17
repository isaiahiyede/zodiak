# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0062_auto_20190217_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='paar2_date',
            new_name='paar_date',
        ),
    ]
