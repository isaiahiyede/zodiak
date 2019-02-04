# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0041_auto_20190202_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('contact_name', models.CharField(max_length=50, blank=True, null=True)),
                ('contact_position', models.CharField(max_length=50, blank=True, null=True)),
                ('contact_department', models.CharField(max_length=50, blank=True, null=True)),
                ('contact_phone_number', models.CharField(max_length=50, blank=True, null=True)),
                ('contact_email', models.EmailField(max_length=50, blank=True, null=True)),
                ('contact_address_1', models.CharField(max_length=20, blank=True, null=True)),
                ('contact_city', models.CharField(max_length=20, blank=True, null=True)),
                ('contact_state', models.CharField(max_length=20, blank=True, null=True)),
                ('contact_cac', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('contact_idcard', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('contact_other_means_of_id', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('user_acc', models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'ordering': ['-user_acc'],
            },
        ),
        migrations.CreateModel(
            name='SecondaryContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sec_contact_name', models.CharField(max_length=50, blank=True, null=True)),
                ('sec_contact_position', models.CharField(max_length=50, blank=True, null=True)),
                ('sec_contact_department', models.CharField(max_length=50, blank=True, null=True)),
                ('sec_contact_phone_number', models.CharField(max_length=50, blank=True, null=True)),
                ('sec_contact_email', models.EmailField(max_length=50, blank=True, null=True)),
                ('sec_contact_address_1', models.CharField(max_length=20, blank=True, null=True)),
                ('sec_contact_city', models.CharField(max_length=20, blank=True, null=True)),
                ('sec_contact_state', models.CharField(max_length=20, blank=True, null=True)),
                ('sec_contact_cac', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('sec_contact_idcard', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('sec_contact_other_means_of_id', models.ImageField(blank=True, null=True, upload_to='item_photo')),
                ('sec_user_acc', models.ForeignKey(blank=True, null=True, to='zodiakApp.UserAccount')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'ordering': ['-sec_user_acc'],
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_acc',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
