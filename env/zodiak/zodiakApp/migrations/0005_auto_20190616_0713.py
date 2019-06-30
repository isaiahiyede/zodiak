# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0004_auto_20190612_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='finances',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='finances',
            name='validity_period',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
