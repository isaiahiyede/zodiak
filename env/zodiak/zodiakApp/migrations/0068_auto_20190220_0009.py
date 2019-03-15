# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0067_minibatches_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('duty_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('duty_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('duty_date_paid', models.DateField(blank=True, null=True)),
                ('duty_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('terminal_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('terminal_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('terminal_charge_date_paid', models.DateField(blank=True, null=True)),
                ('terminal_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('shipping_line_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('shipping_line_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('shipping_line_charge_date_paid', models.DateField(blank=True, null=True)),
                ('shipping_line_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('son_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('son_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('son_charge_date_paid', models.DateField(blank=True, null=True)),
                ('son_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('airline_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('airline_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('airline_charge_date_paid', models.DateField(blank=True, null=True)),
                ('airline_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('quarantine_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('quarantine_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('quarantine_charge_date_paid', models.DateField(blank=True, null=True)),
                ('quarantine_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('ndlea_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('ndlea_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('ndlea_charge_date_paid', models.DateField(blank=True, null=True)),
                ('ndlea_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('nafdac_charge_amount', models.FloatField(blank=True, null=True, default=0.0)),
                ('nafdac_charge_paid_by', models.CharField(max_length=50, blank=True, null=True)),
                ('nafdac_charge_date_paid', models.DateField(blank=True, null=True)),
                ('nafdac_charge_refundablle_as', models.CharField(max_length=50, blank=True, null=True)),
                ('other_charges_due_carrier', models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)),
                ('insurance_charge', models.FloatField(blank=True, null=True, default=0)),
                ('VAT_charge', models.FloatField(blank=True, null=True, default=0)),
                ('demurrage_rate', models.FloatField(max_length=10, blank=True, null=True, default=0.1)),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Finances',
                'ordering': ['-created_on'],
            },
        ),
        # migrations.RemoveField(
        #     model_name='job',
        #     name='VAT_charge',
        # ),
        migrations.RemoveField(
            model_name='job',
            name='chargeable_rate',
        ),
        migrations.RemoveField(
            model_name='job',
            name='demurrage_rate',
        ),
        migrations.RemoveField(
            model_name='job',
            name='insurance_charge',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_paid',
        ),
        migrations.RemoveField(
            model_name='job',
            name='other_charges_due_carrier',
        ),
        migrations.RemoveField(
            model_name='job',
            name='value_for_carriage',
        ),
        migrations.AddField(
            model_name='job',
            name='job_arrival_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_financial_info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='finances',
            name='job_finance',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.Job'),
        ),
    ]
