# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0022_auto_20190106_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_user_acc',
            field=models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
