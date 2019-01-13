# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0029_auto_20190112_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='DockReceipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tracking_number', models.CharField(max_length=100, blank=True, null=True)),
                ('exporter_name_and_address', models.CharField(max_length=100, blank=True, null=True)),
                ('zip_code', models.CharField(max_length=100, blank=True, null=True)),
                ('consigned_to', models.CharField(max_length=100, blank=True, null=True)),
                ('notify_party_name_and_address', models.CharField(max_length=100, blank=True, null=True)),
                ('document_number', models.CharField(max_length=100, blank=True, null=True)),
                ('bl_or_awb_number', models.CharField(max_length=100, blank=True, null=True)),
                ('export_references', models.CharField(max_length=100, blank=True, null=True)),
                ('forwarding_agent_fmc_no', models.CharField(max_length=100, blank=True, null=True)),
                ('state_and_country_of_origin_or_ftz_number', models.CharField(max_length=100, blank=True, null=True)),
                ('domestic_routing', models.CharField(max_length=100, blank=True, null=True)),
                ('loading_pier', models.CharField(max_length=100, blank=True, null=True)),
                ('type_of_move', models.CharField(max_length=100, blank=True, null=True)),
                ('containerized', models.BooleanField(default=False)),
                ('precarriage_by', models.CharField(max_length=100, blank=True, null=True)),
                ('place_of_receipt_by_precarrier', models.CharField(max_length=100, blank=True, null=True)),
                ('exporting_carrier', models.CharField(max_length=100, blank=True, null=True)),
                ('port_of_loading', models.CharField(max_length=100, blank=True, null=True)),
                ('foreign_port_of_unloading', models.CharField(max_length=100, blank=True, null=True)),
                ('place_of_delivery_by_oncarrier', models.CharField(max_length=100, blank=True, null=True)),
                ('mks_nos', models.CharField(max_length=100, blank=True, null=True)),
                ('no_of_pkgs', models.IntegerField(blank=True, null=True)),
                ('description_of_package_and_goods', models.CharField(max_length=100, blank=True, null=True)),
                ('gross_weight', models.IntegerField(blank=True, null=True)),
                ('measurement', models.CharField(max_length=100, blank=True, null=True)),
                ('lighter_truck', models.CharField(max_length=100, blank=True, null=True)),
                ('arrived_date', models.CharField(max_length=100, blank=True, null=True)),
                ('arrived_time', models.CharField(max_length=100, blank=True, null=True)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(max_length=100, blank=True, null=True)),
                ('batch', models.CharField(max_length=100, blank=True, null=True)),
                ('unloaded_date', models.CharField(max_length=100, blank=True, null=True)),
                ('unloaded_time', models.CharField(max_length=100, blank=True, null=True)),
                ('checked_by', models.CharField(max_length=100, blank=True, null=True)),
                ('placed_location', models.CharField(max_length=100, blank=True, null=True)),
                ('receiving_clerk_name', models.CharField(max_length=100, blank=True, null=True)),
                ('date_from_receiving_clerk', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='agent_acct_no',
            new_name='carrier_agent_acct_no',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='accounting_info',
            new_name='carrier_agent_city',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='airport_of_departure',
            new_name='carrier_agent_name',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='airport_of_destination',
            new_name='consignees_address',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='carrier_agent_name_and_city',
            new_name='consignees_name',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='insure',
            new_name='demurrage',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='insurance',
            new_name='insurance_charge',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='consignees_name_and_address',
            new_name='shippers_address',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='currency_code',
            new_name='shippers_names',
        ),
        migrations.RemoveField(
            model_name='job',
            name='amount_of_insurance',
        ),
        migrations.RemoveField(
            model_name='job',
            name='destination_and_departure_routing_code1',
        ),
        migrations.RemoveField(
            model_name='job',
            name='issued_airline_carrier_and_address',
        ),
        migrations.RemoveField(
            model_name='job',
            name='origin_airline_carrier',
        ),
        migrations.RemoveField(
            model_name='job',
            name='origin_routing_code',
        ),
        migrations.RemoveField(
            model_name='job',
            name='ref_number',
        ),
        migrations.RemoveField(
            model_name='job',
            name='regulation_of_goods',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requested_flight_and_date1',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requested_flight_and_date2',
        ),
        migrations.RemoveField(
            model_name='job',
            name='second_airline_carrier',
        ),
        migrations.RemoveField(
            model_name='job',
            name='shippers_name_and_address',
        ),
        migrations.RemoveField(
            model_name='job',
            name='state_of_destination',
        ),
        migrations.RemoveField(
            model_name='job',
            name='third_airline_carrier',
        ),
        migrations.RemoveField(
            model_name='job',
            name='total_prepaid',
        ),
        migrations.RemoveField(
            model_name='job',
            name='tracking_number_prefix',
        ),
        migrations.RemoveField(
            model_name='job',
            name='value_for_custom',
        ),
        migrations.AddField(
            model_name='job',
            name='insured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='vat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dockreceipt',
            name='shipping_package',
            field=models.ForeignKey(blank=True, null=True, to='zodiakApp.Job'),
        ),
    ]
