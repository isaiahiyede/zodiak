# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0046_auto_20190203_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarycontact',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='primarycontact',
            name='primary_created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='secondarycontact',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='secondarycontact',
            name='sec_contact_created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
