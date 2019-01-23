# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0037_auto_20190120_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_doc_1',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_2',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_3',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_4',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_5',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_6',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_7',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_8',
            field=models.FileField(blank=True, null=True, upload_to='item_photo'),
        ),
    ]
