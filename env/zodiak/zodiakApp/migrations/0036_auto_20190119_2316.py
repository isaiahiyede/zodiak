# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0035_auto_20190119_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='VAT_charge',
            field=models.FloatField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='demurrage_grace_period',
            field=models.IntegerField(blank=True, null=True, default=7),
        ),
        migrations.AlterField(
            model_name='job',
            name='demurrage_rate',
            field=models.FloatField(max_length=10, blank=True, null=True, default=0.1),
        ),
        migrations.AlterField(
            model_name='job',
            name='insurance_charge',
            field=models.FloatField(blank=True, null=True, default=0),
        ),
    ]
