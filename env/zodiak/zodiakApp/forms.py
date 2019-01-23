from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User
from zodiakApp.models import Job, UserAccount, Address, RelationshipManager, Quotation

attr3 = {'style': 'border-color: green;', 'required': 'required'}
attr4 = {'style': 'border-color: green;'}


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')


class RelationshipManagerForm(forms.ModelForm):
    class Meta:
        model = RelationshipManager
        fields = ('rm_name','rm_email','rm_position','rm_designation','rm_alt_email','rm_contact_no','rm_office_address')


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ('user_acct','item','quantity','price_per_item','total_cost','notes_on_job')


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            'job_user_acc', 'job_origin', 'job_destination', 'job_start_date', 'job_end_date', 'job_date_of_arrival',
            'job_status', 'job_cost', 'job_amount_paid','job_paid', 'job_amount_balance', 'job_shipper', 'job_description', 'job_name',
            'job_awl_number', 'job_paid_for', 'job_bol_number', 'job_vessel_name', 'job_type', 'job_doc_1', 'job_doc_2',
            'job_doc_3','job_comment', 'job_in_transit','job_doc_4', 'job_doc_5', 'job_doc_6',

            'job_arrived', 'job_undergoing_clearnace', 'job_undergoing_ammendment', 'job_examined', 'job_cleared', 'job_completed',
            'job_invoiced', 'job_paid_for', 'job_processing','job_issue_resolution', 'box_weight_Actual', 'insured', 'vat', 'demurrage',
            'insurance_charge', 'VAT_charge', 'demurrage_rate', 'demurrage_grace_period', 'shippers_name', 'shippers_address', 'shippers_number',
            'shippers_acct_no','consignees_name', 'consignees_address',

            'box_length','box_width','box_height','box_weight','box_weight_K',

            'consignees_acct_no', 'consignees_number', 'carrier_agent_name', 'carrier_agent_country', 'carrier_agent_iata_code', 'carrier_agent_acct_no',
            'handling_info', 'value_for_carriage', 'number_of_pieces_to_ship','gross_weight', 'chargeable_rate', 'note_on_the_package', 'nature_of_goods', 
            'airline_tracking_number','other_charges_due_carrier', 'place_of_execution', 'shippers_name', 'carrier_name','quantity_of_goods',

            )


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user', 'phone_number', 'user_passport', 'user_cac')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('user_acc', 'address_1', 'address_2', 'city', 'state', 'zip_code')
