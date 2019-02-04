# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0040_quotation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_1',
            new_name='contact_address_1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_2',
            new_name='contact_city',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='city',
            new_name='contact_state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='address',
            name='contact_department',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='contact_email',
            field=models.EmailField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='contact_name',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='contact_phone_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='contact_position',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='office_aadress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='state',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='type_of_business',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='website',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
