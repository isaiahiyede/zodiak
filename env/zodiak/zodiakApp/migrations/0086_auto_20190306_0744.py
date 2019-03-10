# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zodiakApp', '0085_auto_20190303_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finances',
            old_name='VAT_charge',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='finances',
            old_name='airline_charge_paid_by',
            new_name='charge_type',
        ),
        migrations.RenameField(
            model_name='finances',
            old_name='airline_charge_date_paid',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='finances',
            old_name='airline_charge_refundablle_as',
            new_name='paid_by',
        ),
        migrations.RenameField(
            model_name='finances',
            old_name='duty_paid_by',
            new_name='refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='airline_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='demurrage_rate',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='duty_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='duty_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='duty_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='insurance_charge',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='nafdac_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='nafdac_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='nafdac_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='nafdac_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='ndlea_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='ndlea_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='ndlea_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='ndlea_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='other_charges_due_carrier',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='quarantine_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='quarantine_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='quarantine_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='quarantine_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='shipping_line_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='shipping_line_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='shipping_line_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='shipping_line_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='son_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='son_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='son_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='son_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='terminal_charge_amount',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='terminal_charge_date_paid',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='terminal_charge_paid_by',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='terminal_charge_refundablle_as',
        ),
        migrations.RemoveField(
            model_name='minibatches',
            name='no_of_containers',
        ),
        migrations.RemoveField(
            model_name='minibatches',
            name='type_of_container',
        ),
        migrations.AddField(
            model_name='comments',
            name='commented_by',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='job_new_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='minibatches',
            name='job_description',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='staff_account',
            field=models.BooleanField(default=True),
        ),
    ]
