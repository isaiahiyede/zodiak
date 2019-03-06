from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User

from zodiakApp.models import Job, UserAccount, Documents, Comments, ContainerTypes, Finances, MiniBatches, Batch, PrimaryContact, RelationshipManager, Quotation, SecondaryContact, OfficeUseOnly,Batch

attr3 = {'style': 'border-color: green;', 'required': 'required'}
attr4 = {'style': 'border-color: green;'}


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('msg', 'commented_by',)


class MiniBatchesForm(forms.ModelForm):
    class Meta:
        model = MiniBatches
        fields = ('no_of_packages','job_description','carrier_name','gross_wgh','net_wgh','exp_date_of_arrival','date_of_arrival','cbm')


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

            'amount','paid_by','date_paid','refundablle_as','charge_type',
            )

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = (

            'job_paar','shippers_name','shippers_email','shippers_number','shippers_country',
            'shippers_address','consignees_name','consignees_number','consignee_email','consignee_country',
            'consignees_address','country_of_origin','country_of_arrival','port_of_destination','port_of_arrival',
            'job_vessel_name','job_awl_bol_number','paar_date','insured', 'insurance_date','packing_list', 
            'packing_list_date','job_son', 'son_date', 'job_ccro', 'ccro_date', 'duty_exemption', 'duty_exemption_date', 
            'batch_type', 'job_route','ref_number','customer_type','company_name',

            'job_user_acc','job_start_date', 'job_end_date', 'job_date_of_arrival',
            'job_status', 'job_cost', 'job_amount_paid','job_paid', 'job_amount_balance', 'job_description',
            'job_paid_for', 'job_vessel_name', 'job_type',

            'job_arrived', 'job_undergoing_clearnace', 'job_undergoing_ammendment', 'job_examined', 'job_cleared', 'job_completed',
            'job_invoiced', 'job_paid_for', 'job_processing','job_issue_resolution', 'box_weight_Actual', 'insured', 'vat', 'demurrage',
            'demurrage_grace_period', 'shippers_name', 'shippers_address', 'shippers_number',
            'consignees_name', 'consignees_address','job_arrival_status_mode',

            'box_length','box_width','box_height','box_weight','box_weight_K',

            'consignees_number', 'job_cost',
            'handling_info', 'number_of_pieces_to_ship','gross_weight',  'note_on_the_package', 'nature_of_goods', 
            'airline_tracking_number', 'place_of_execution', 'shippers_name', 'quantity_of_goods',

            )


class JobForm2(forms.ModelForm):

    class Meta:
        model = Job
        fields = (

            'job_paar','paar_date','insured', 'insurance_date','packing_list', 
            'packing_list_date','job_son', 'son_date', 'job_ccro', 'ccro_date','duty_exemption', 'duty_exemption_date',
            )



class JobForm4(forms.ModelForm):

    class Meta:
        model = Job
        fields = (

            'handling_info','note_on_the_package', 'job_comment', 'job_description',
            
            )


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user', 'phone_number', 'user_passport', 'user_cac','type_of_business','acc_owner',
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


class ContainerTypesForm(forms.ModelForm):
    class Meta:
        model = ContainerTypes
        fields = ('name_of_container','number_of_container','job_obj_cont',)


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('name_of_doc','doc_obj','job_obj_doc',)




