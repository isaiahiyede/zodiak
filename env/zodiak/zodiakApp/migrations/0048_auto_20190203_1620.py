# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0047_auto_20190203_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeUseOnly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('internal_evaluation', models.TextField(blank=True, null=True)),
                ('mode_of_operation', models.CharField(max_length=20, blank=True, null=True)),
                ('special_request', models.CharField(max_length=20, blank=True, null=True)),
                ('staff_evaluation', models.TextField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Office Use only',
                'ordering': ['-created_on'],
            },
        ),
        migrations.RemoveField(
            model_name='relationshipmanager',
            name='deleted',
        ),
        migrations.AddField(
            model_name='officeuseonly',
            name='rm_client_obj',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.RelationshipManager'),
        ),
    ]
