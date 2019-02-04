# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0048_auto_20190203_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officeuseonly',
            old_name='deleted',
            new_name='off_deleted',
        ),
        migrations.AddField(
            model_name='relationshipmanager',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
