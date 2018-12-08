# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=20, null=True, blank=True)),
                ('address_2', models.CharField(max_length=20, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('state', models.CharField(max_length=20, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'ordering': ['-user_acc'],
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_origin', models.CharField(max_length=50, null=True, blank=True)),
                ('job_destination', models.CharField(max_length=50, null=True, blank=True)),
                ('job_start_date', models.DateField(max_length=50, null=True, blank=True)),
                ('job_end_date', models.DateField(max_length=50, null=True, blank=True)),
                ('job_date_of_arrival', models.DateField(max_length=50, null=True, blank=True)),
                ('job_status', models.CharField(default='New', max_length=50)),
                ('job_cost', models.FloatField(default=1.0)),
                ('job_shipper', models.TextField(null=True, blank=True)),
                ('job_description', models.CharField(max_length=20, null=True, blank=True)),
                ('job_id', models.CharField(max_length=20, null=True, blank=True)),
                ('job_name', models.CharField(max_length=20, null=True, blank=True)),
                ('job_awl_number', models.CharField(max_length=20, null=True, blank=True)),
                ('job_bol_number', models.CharField(max_length=20, null=True, blank=True)),
                ('job_vessel_name', models.CharField(max_length=20, null=True, blank=True)),
                ('job_type', models.CharField(max_length=20, null=True, blank=True)),
                ('job_doc_1', models.ImageField(null=True, upload_to='item_photo', blank=True)),
                ('job_doc_2', models.ImageField(null=True, upload_to='item_photo', blank=True)),
                ('job_doc_3', models.ImageField(null=True, upload_to='item_photo', blank=True)),
                ('job_created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-job_created_on'],
                'verbose_name_plural': 'Job',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_updated', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_passport', models.ImageField(null=True, upload_to='item_photo', blank=True)),
                ('user_cac', models.ImageField(null=True, upload_to='item_photo', blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'UserAccount',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='job_user_acc',
            field=models.ForeignKey(blank=True, to='zodiakApp.UserAccount', null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='user_acc',
            field=models.ForeignKey(blank=True, to='zodiakApp.UserAccount', null=True),
        ),
    ]
