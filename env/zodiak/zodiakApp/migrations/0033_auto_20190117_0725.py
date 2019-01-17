# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0032_auto_20190115_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_doc_4',
            field=models.ImageField(null=True, upload_to='item_photo', blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_doc_5',
            field=models.ImageField(null=True, upload_to='item_photo', blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_doc_6',
            field=models.ImageField(null=True, upload_to='item_photo', blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='quantity_of_goods',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='box_weight_Actual',
            field=models.DecimalField(default=0.0, null=True, max_digits=15, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='gross_weight',
            field=models.DecimalField(default=0.0, null=True, max_digits=15, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='handling_info',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='note_on_the_package',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
