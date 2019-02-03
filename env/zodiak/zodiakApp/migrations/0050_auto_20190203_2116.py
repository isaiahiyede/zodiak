# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0049_auto_20190203_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('batch_id', models.CharField(max_length=20, blank=True, null=True)),
                ('no_of_jobs', models.IntegerField(blank=True, null=True)),
                ('mode_of_batch', models.CharField(max_length=20, blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Batch',
                'ordering': ['-created_on'],
            },
        ),
        migrations.AlterField(
            model_name='officeuseonly',
            name='rm_client_obj',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount'),
        ),
    ]
