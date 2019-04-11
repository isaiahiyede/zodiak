# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0095_auto_20190411_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stat_type', models.CharField(max_length=50, blank=True, null=True)),
                ('stat_date', models.CharField(max_length=50, blank=True, null=True)),
                ('stat_comment', models.TextField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('job_stat', models.ForeignKey(blank=True, null=True, to='zodiakApp.Job')),
            ],
            options={
                'verbose_name_plural': 'StatusRec',
                'ordering': ['-created_on'],
            },
        ),
    ]
