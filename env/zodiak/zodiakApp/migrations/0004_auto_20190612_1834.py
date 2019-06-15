# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0003_shippers_deleted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finances',
            options={'verbose_name_plural': 'Finances', 'ordering': ['charge_type']},
        ),
        migrations.AddField(
            model_name='finances',
            name='validity_period',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
