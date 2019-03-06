# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0085_auto_20190303_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='commented_by',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
