# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0096_statusrec'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='doc_action',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_date',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_recieved',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
