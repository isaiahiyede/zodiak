# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0017_auto_20190101_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationshipmanager',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='relationshipmanager',
            name='rm_client',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount'),
        ),
    ]
