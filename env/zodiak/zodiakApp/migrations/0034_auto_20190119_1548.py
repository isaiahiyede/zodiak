# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0033_auto_20190117_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='nature_and_quantity_of_goods',
            new_name='nature_of_goods',
        ),
    ]
