# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0081_auto_20190302_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_of_doc', models.CharField(max_length=100, blank=True, null=True)),
                ('doc_obj', models.FileField(blank=True, null=True, upload_to='item_photo')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Documents',
                'ordering': ['-created_on'],
            },
        ),
        migrations.RemoveField(
            model_name='job',
            name='commercial_invoice_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='form_m_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_1',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_2',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_3',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_4',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_5',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_6',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_7',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_doc_8',
        ),
        migrations.AddField(
            model_name='documents',
            name='job_obj_doc',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.Job'),
        ),
    ]
