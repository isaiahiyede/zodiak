# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0042_auto_20190202_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primarycontact',
            name='contact_cac',
        ),
        migrations.RemoveField(
            model_name='primarycontact',
            name='contact_idcard',
        ),
        migrations.RemoveField(
            model_name='primarycontact',
            name='contact_other_means_of_id',
        ),
        migrations.RemoveField(
            model_name='secondarycontact',
            name='sec_contact_cac',
        ),
        migrations.RemoveField(
            model_name='secondarycontact',
            name='sec_contact_idcard',
        ),
        migrations.RemoveField(
            model_name='secondarycontact',
            name='sec_contact_other_means_of_id',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_other_means_of_id',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_cac',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_passport',
            field=models.ImageField(blank=True, null=True, upload_to='item_photo'),
        ),
    ]
