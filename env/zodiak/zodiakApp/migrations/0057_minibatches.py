# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0056_auto_20190212_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniBatches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('no_of_packages', models.IntegerField(blank=True, null=True)),
                ('mini_batch_id', models.CharField(max_length=50, blank=True, null=True)),
                ('cbm', models.CharField(max_length=50, blank=True, null=True)),
                ('gross_wgh', models.FloatField(blank=True, null=True, default=0.0)),
                ('net_wgh', models.FloatField(blank=True, null=True, default=0.0)),
                ('exp_date_of_arrival', models.DateField(blank=True, null=True)),
                ('date_of_arrival', models.DateField(blank=True, null=True)),
                ('batch_created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(blank=True, null=True, to='zodiakApp.Job')),
            ],
            options={
                'verbose_name_plural': 'Mini Btaches',
                'ordering': ['-batch_created_on'],
            },
        ),
    ]
