from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User
from zodiakApp.models import Job, UserAccount, Finances, MiniBatches, Batch, PrimaryContact, RelationshipManager, Quotation, SecondaryContact, OfficeUseOnly,Batch

attr3 = {'style': 'border-color: green;', 'required': 'required'}
attr4 = {'style': 'border-color: green;'}


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')


class MiniBatchesForm(forms.ModelForm):
    class Meta:
        model = MiniBatches
        fields = ('no_of_packages','no_of_containers','type_of_container','carrier_name','gross_wgh','net_wgh','exp_date_of_arrival','date_of_arrival','cbm')


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ('mode_of_batch',)


class RelationshipManagerForm(forms.ModelForm):
    class Meta:
        model = RelationshipManager
        fields = ('rm_name','rm_email','rm_position','rm_designation','rm_alt_email','rm_contact_no','rm_office_address')


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ('user_acct','item','quantity','price_per_item','total_cost','notes_on_job')


class FinancialsForm(forms.ModelForm):
    class Meta:
        model = Finances
        fields = (

            'duty_amount','duty_paid_by','duty_date_paid','duty_refundablle_as',
            'terminal_charge_amount','terminal_charge_paid_by','terminal_charge_date_paid','terminal_charge_refundablle_as',
            'shipping_line_charge_amount','shipping_line_charge_paid_by','shipping_line_charge_date_paid','shipping_line_charge_refundablle_as',
            'son_charge_amount','son_charge_paid_by','son_charge_date_paid','son_charge_refundablle_as',
            'airline_charge_amount','airline_charge_paid_by','airline_charge_date_paid','airline_charge_refundablle_as',
            'quarantine_charge_amount','quarantine_charge_paid_by','quarantine_charge_date_paid','quarantine_charge_refundablle_as',
            'ndlea_charge_amount','ndlea_charge_paid_by','ndlea_charge_date_paid','ndlea_charge_refundablle_as',
            'nafdac_charge_amount','nafdac_charge_paid_by','nafdac_charge_date_paid','nafdac_charge_refundablle_as',
            'other_charges_due_carrier','insurance_charge','VAT_charge','demurrage_rate',

            )

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = (

            'job_paar',   'shippers_name','shippers_email','shippers_number','shippers_country',
            'shippers_address','consignees_name','consignees_number','consignee_email','consignee_country',
            'consignees_address','country_of_origin','country_of_arrival','port_of_destination','port_of_arrival',
            'job_vessel_name','job_awl_bol_number','paar_date','insured', 'insurance_date','packing_list', 
            'packing_list_date','form_m','job_son', 'son_date', 'job_ccro', 'ccro_date', 'duty_exemption', 'duty_exemption_date', 
            'commercial_invoice','batch_type', 'job_route', 

            'job_user_acc','job_start_date', 'job_end_date', 'job_date_of_arrival',
            'job_status', 'job_cost', 'job_amount_paid','job_paid', 'job_amount_balance', 'job_description',
            'job_paid_for', 'job_vessel_name', 'job_type', 'job_doc_1', 'job_doc_2',
            'job_doc_3','job_comment', 'job_in_transit','job_doc_4', 'job_doc_5', 'job_doc_6','job_doc_7', 'job_doc_8',

            'job_arrived', 'job_undergoing_clearnace', 'job_undergoing_ammendment', 'job_examined', 'job_cleared', 'job_completed',
            'job_invoiced', 'job_paid_for', 'job_processing','job_issue_resolution', 'box_weight_Actual', 'insured', 'vat', 'demurrage',
            'demurrage_grace_period', 'shippers_name', 'shippers_address', 'shippers_number',
            'consignees_name', 'consignees_address',

            'box_length','box_width','box_height','box_weight','box_weight_K',

            'consignees_number', 'job_cost',
            'handling_info', 'number_of_pieces_to_ship','gross_weight',  'note_on_the_package', 'nature_of_goods', 
            'airline_tracking_number', 'place_of_execution', 'shippers_name', 'quantity_of_goods',

            )


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user', 'phone_number', 'user_passport', 'user_cac','type_of_business',
            'user_other_means_of_id','city','state','website','office_aadress')


class PrimaryContactForm(forms.ModelForm):
    class Meta:
        model = PrimaryContact
        fields = ('contact_name', 'contact_position', 'contact_department',
            'contact_phone_number','contact_email','contact_address_1')


class SecondaryContactForm(forms.ModelForm):
    class Meta:
        model = SecondaryContact
        fields = ('sec_contact_name', 'sec_contact_position', 'sec_contact_department',
            'sec_contact_phone_number','sec_contact_email','sec_contact_address_1')


class OfficeUseOnlyForm(forms.ModelForm):
    class Meta:
        model = OfficeUseOnly
        fields = ('rm_client_obj', 'internal_evaluation', 'mode_of_operation',
            'special_request','staff_evaluation')


class BatchProcessForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ('status_of_batch',)



