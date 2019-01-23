# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0039_auto_20190120_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('item', models.CharField(max_length=20, blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price_per_item', models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1)),
                ('total_cost', models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1)),
                ('notes_on_job', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('user_acct', models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount')),
            ],
            options={
                'verbose_name_plural': 'Quotation',
                'ordering': ['-user_acct'],
            },
        ),
    ]
