# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0023_auto_20190106_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_user_acc',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount'),
        ),
    ]
