# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0043_auto_20190202_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarycontact',
            name='user_acc',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='secondarycontact',
            name='sec_user_acc',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
