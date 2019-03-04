# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0079_job_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('dry_freight_20', models.IntegerField(blank=True, null=True)),
                ('dry_freight_40', models.IntegerField(blank=True, null=True)),
                ('high_cube_dry_cont_40', models.IntegerField(blank=True, null=True)),
                ('high_cube_dry_cont_45', models.IntegerField(blank=True, null=True)),
                ('reefer_cont_20', models.IntegerField(blank=True, null=True)),
                ('reefer_cont_40', models.IntegerField(blank=True, null=True)),
                ('flat_rack_cont_20', models.IntegerField(blank=True, null=True)),
                ('flat_rack_cont_40', models.IntegerField(blank=True, null=True)),
                ('col_flat_rack_20', models.IntegerField(blank=True, null=True)),
                ('col_flat_rack_40', models.IntegerField(blank=True, null=True)),
                ('open_top_cont_20', models.IntegerField(blank=True, null=True)),
                ('open_top_cont_40', models.IntegerField(blank=True, null=True)),
                ('artificial_tweendeck', models.IntegerField(blank=True, null=True)),
                ('open_sided_open_top_20', models.IntegerField(blank=True, null=True)),
                ('open_sided_open_top_40', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('job_obj_cont', models.ForeignKey(blank=True, null=True, to='zodiakApp.Job')),
            ],
            options={
                'verbose_name_plural': 'Types of Containers',
                'ordering': ['-created_on'],
            },
        ),
    ]
