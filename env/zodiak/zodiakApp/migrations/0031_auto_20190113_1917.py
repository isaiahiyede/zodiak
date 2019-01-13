# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0030_auto_20190113_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='carrier_agent_city',
            new_name='carrier_agent_country',
        ),
        migrations.RemoveField(
            model_name='job',
            name='box_weight_Actual_K',
        ),
        migrations.RemoveField(
            model_name='job',
            name='shippers_names',
        ),
    ]
