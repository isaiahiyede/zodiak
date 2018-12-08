# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0012_auto_20181208_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.TextField(null=True, blank=True)),
                ('msg_created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('job_message', models.ForeignKey(blank=True, to='zodiakApp.Job', null=True)),
            ],
            options={
                'ordering': ['-msg_created_on'],
                'verbose_name_plural': 'Commnets',
            },
        ),
    ]
