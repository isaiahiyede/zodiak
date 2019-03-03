# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0080_containertypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='containertypes',
            name='artificial_tweendeck',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='col_flat_rack_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='col_flat_rack_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='dry_freight_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='dry_freight_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='flat_rack_cont_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='flat_rack_cont_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='high_cube_dry_cont_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='high_cube_dry_cont_45',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='open_sided_open_top_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='open_sided_open_top_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='open_top_cont_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='open_top_cont_40',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='reefer_cont_20',
        ),
        migrations.RemoveField(
            model_name='containertypes',
            name='reefer_cont_40',
        ),
        migrations.AddField(
            model_name='containertypes',
            name='name_of_container',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='containertypes',
            name='number_of_container',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
