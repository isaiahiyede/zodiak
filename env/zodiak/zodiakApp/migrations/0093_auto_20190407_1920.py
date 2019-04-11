# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0092_auto_20190407_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finances',
            old_name='job_comment',
            new_name='comments',
        ),
    ]
