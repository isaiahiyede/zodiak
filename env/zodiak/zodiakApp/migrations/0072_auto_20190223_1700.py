# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0071_auto_20190220_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_doc_7',
            new_name='commercial_invoice_number',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_doc_8',
            new_name='form_m_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='commercial_invoice',
        ),
        migrations.RemoveField(
            model_name='job',
            name='form_m',
        ),
    ]
