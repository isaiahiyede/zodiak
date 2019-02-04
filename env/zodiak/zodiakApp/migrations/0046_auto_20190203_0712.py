# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0045_auto_20190203_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primarycontact',
            name='contact_city',
        ),
        migrations.RemoveField(
            model_name='primarycontact',
            name='contact_state',
        ),
        migrations.RemoveField(
            model_name='secondarycontact',
            name='sec_contact_city',
        ),
        migrations.RemoveField(
            model_name='secondarycontact',
            name='sec_contact_state',
        ),
    ]
