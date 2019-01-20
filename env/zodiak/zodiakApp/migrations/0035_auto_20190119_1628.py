# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0034_auto_20190119_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_doc_7',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_doc_8',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
    ]
