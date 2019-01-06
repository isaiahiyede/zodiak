# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0019_useraccount_rm_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='arrived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='cleared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='examined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='in_transit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='invoiced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='issue_resolution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='paid_for',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='processing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='undergoing_ammendment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='undergoing_clearnace',
            field=models.BooleanField(default=False),
        ),
    ]
