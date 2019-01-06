# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0024_auto_20190106_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments', 'ordering': ['-msg_created_on']},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name_plural': 'Jobs', 'ordering': ['-job_created_on']},
        ),
        migrations.AlterModelOptions(
            name='jobmodes',
            options={'verbose_name_plural': 'Job Modes', 'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='relationshipmanager',
            options={'verbose_name_plural': 'Relationship Managers', 'ordering': ['-rm_created_on']},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses', 'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name_plural': 'User Accounts', 'ordering': ['-created_on']},
        ),
    ]
