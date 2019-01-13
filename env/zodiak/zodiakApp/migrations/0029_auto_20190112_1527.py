# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0028_job_job_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='VAT_charge',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='accounting_info',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='agent_acct_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='airline_tracking_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='airport_of_departure',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='airport_of_destination',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='amount_of_insurance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='box_height',
            field=models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_length',
            field=models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_weight',
            field=models.DecimalField(blank=True, null=True, default=0, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_weight_Actual',
            field=models.DecimalField(default=0.0, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_weight_Actual_K',
            field=models.DecimalField(default=0.0, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_weight_K',
            field=models.DecimalField(blank=True, null=True, default=0, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='box_width',
            field=models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=1),
        ),
        migrations.AddField(
            model_name='job',
            name='carrier_agent_iata_code',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='carrier_agent_name_and_city',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='carrier_name',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='chargeable_rate',
            field=models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='job',
            name='consignees_acct_no',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='consignees_name_and_address',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='consignees_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='currency_code',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='demurrage_grace_period',
            field=models.IntegerField(default=7),
        ),
        migrations.AddField(
            model_name='job',
            name='demurrage_rate',
            field=models.FloatField(max_length=10, default=0.1),
        ),
        migrations.AddField(
            model_name='job',
            name='destination_and_departure_routing_code1',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='gross_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='handling_info',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='insurance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='insure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='issued_airline_carrier_and_address',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='nature_and_quantity_of_goods',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='note_on_the_package',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='number_of_pieces_to_ship',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='origin_airline_carrier',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='origin_routing_code',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='other_charges_due_carrier',
            field=models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='job',
            name='place_of_execution',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='ref_number',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='regulation_of_goods',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requested_flight_and_date1',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requested_flight_and_date2',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='second_airline_carrier',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_acct_no',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_name',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_name_and_address',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='shippers_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='state_of_destination',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='third_airline_carrier',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='total_prepaid',
            field=models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='job',
            name='tracking_number_prefix',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='value_for_carriage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='value_for_custom',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
