# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0021_jobmodes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='arrived',
            new_name='job_arrived',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='cleared',
            new_name='job_cleared',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='completed',
            new_name='job_completed',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='examined',
            new_name='job_examined',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='in_transit',
            new_name='job_in_transit',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='invoiced',
            new_name='job_invoiced',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='issue_resolution',
            new_name='job_issue_resolution',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='paid_for',
            new_name='job_processing',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='processing',
            new_name='job_undergoing_ammendment',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='undergoing_ammendment',
            new_name='job_undergoing_clearnace',
        ),
        migrations.RemoveField(
            model_name='job',
            name='undergoing_clearnace',
        ),
    ]
