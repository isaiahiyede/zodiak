# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0054_auto_20190210_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_destination',
            new_name='commercial_invoice',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_origin',
            new_name='consignee_country',
        ),
        migrations.RemoveField(
            model_name='job',
            name='carrier_agent_acct_no',
        ),
        migrations.RemoveField(
            model_name='job',
            name='carrier_agent_country',
        ),
        migrations.RemoveField(
            model_name='job',
            name='carrier_agent_iata_code',
        ),
        migrations.RemoveField(
            model_name='job',
            name='carrier_agent_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='carrier_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='consignees_acct_no',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_awl_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_bol_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_shipper',
        ),
        migrations.RemoveField(
            model_name='job',
            name='shippers_acct_no',
        ),
        migrations.AddField(
            model_name='job',
            name='ccro_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='consignee_email',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country_of_arrival',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country_of_origin',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='duty_exemption',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='duty_exemption_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='form_m',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='insurance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_awl_bol_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_ccro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_paar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='jon_son',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='paar_date',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='packing_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='packing_list_date',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='port_of_arrival',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='port_of_destination',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_country',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_email',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='son_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='consignees_address',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='consignees_name',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='consignees_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_vessel_name',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='shippers_address',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='shippers_name',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='shippers_number',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
