# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0015_auto_20181220_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationshipManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rm_name', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_email', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_position', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_alt_email', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_contact_no', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_designation', models.CharField(max_length=20, blank=True, null=True)),
                ('rm_office_address', models.TextField(blank=True, null=True)),
                ('rm_created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('rm_client', models.ForeignKey(blank=True, null=True, to='zodiakApp.Job')),
            ],
            options={
                'verbose_name_plural': 'Relationship Manager',
                'ordering': ['-rm_created_on'],
            },
        ),
    ]
