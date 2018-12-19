from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User
from zodiakApp.models import Job, UserAccount, Address

attr3 = {'style': 'border-color: green;', 'required': 'required'}
attr4 = {'style': 'border-color: green;'}


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name','last_name')


class JobForm(forms.ModelForm):

    
    class Meta:
        model = Job
        fields = (
            'job_user_acc', 'job_origin', 'job_destination', 'job_start_date', 'job_end_date', 'job_date_of_arrival',
            'job_status', 'job_cost', 'job_amount_paid', 'job_amount_balance', 'job_shipper', 'job_description', 'job_name',
            'job_awl_number', 'job_paid_for', 'job_bol_number', 'job_vessel_name', 'job_type', 'job_doc_1', 'job_doc_2',
            'job_doc_3','job_comment')


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user', 'profile_updated', 'phone_number', 'user_passport', 'user_cac')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('user_acc', 'address_1', 'address_2', 'city', 'state', 'zip_code')
