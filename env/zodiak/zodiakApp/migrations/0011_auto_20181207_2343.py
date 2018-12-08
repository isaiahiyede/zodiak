# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0010_auto_20181207_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_user_acc',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
