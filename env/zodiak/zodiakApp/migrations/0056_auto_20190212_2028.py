# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0055_auto_20190212_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='jon_son',
            new_name='job_son',
        ),
    ]
