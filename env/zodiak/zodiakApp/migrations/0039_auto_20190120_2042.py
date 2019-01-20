# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0038_auto_20190120_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_doc_1',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_2',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_3',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_4',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_5',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_6',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_7',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_doc_8',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
    ]
