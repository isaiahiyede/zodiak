# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0053_auto_20190210_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batch'},
        ),
    ]
