# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0020_auto_20190106_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Job Mode',
                'ordering': ['-name'],
            },
        ),
    ]
