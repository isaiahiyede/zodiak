# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0087_auto_20190309_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='city',
            new_name='country',
        ),
    ]
