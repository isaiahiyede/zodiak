# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0044_auto_20190202_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primarycontact',
            options={'verbose_name_plural': 'Primary Contact', 'ordering': ['-user_acc']},
        ),
        migrations.AlterModelOptions(
            name='secondarycontact',
            options={'verbose_name_plural': 'Secondary Contact', 'ordering': ['-sec_user_acc']},
        ),
    ]
