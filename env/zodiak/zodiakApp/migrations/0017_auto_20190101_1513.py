# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0016_relationshipmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user_cac',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_passport',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
    ]
