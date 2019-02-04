from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.utils import timezone
from django.conf import settings
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
import math

# Create your models here.
		
class UserAccount(models.Model):
    """ user details """
    user = models.OneToOneField(User, unique=True, null=True, blank=True)
    profile_updated = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    type_of_business = models.TextField(null=True,blank=True)
    office_aadress = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    user_passport = models.ImageField(upload_to="item_photo", null=True, blank=True)
    user_cac = models.ImageField(upload_to="item_photo", null=True, blank=True)
    user_other_means_of_id = models.ImageField(upload_to="item_photo", null=True, blank=True)
    inputter = models.BooleanField(default=True)
    authorizer = models.BooleanField(default=False)
    rm_updated = models.BooleanField(default=False)
    reporter = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    city = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    website = models.CharField(max_length=50,null=True,blank=True)
    acc_owner = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
	    verbose_name_plural = 'User Accounts'
	    ordering = ['-created_on']
	    
    def __unicode__(self):
	    return '%s' %(self.user.username)


class PrimaryContact(models.Model):
	contact_name = models.CharField(max_length=50,null=True,blank=True)
	contact_position = models.CharField(max_length=50,null=True,blank=True)
	contact_department = models.CharField(max_length=50,null=True,blank=True)
	contact_phone_number = models.CharField(max_length=50, null=True, blank=True)
	contact_email = models.EmailField(max_length=50,null=True,blank=True)
	user_acc = models.ForeignKey(User, null=True, blank=True)
	contact_address_1 = models.CharField(max_length=20,null=True,blank=True)
	primary_created_on = models.DateTimeField(default=timezone.now)
	deleted = models.BooleanField(default=False)


	class Meta:
	    verbose_name_plural = 'Primary Contact'
	    ordering = ['-user_acc']
	    
	def __unicode__(self):
	    return '%s' %(self.user_acc)

class SecondaryContact(models.Model):
	sec_contact_name = models.CharField(max_length=50,null=True,blank=True)
	sec_contact_position = models.CharField(max_length=50,null=True,blank=True)
	sec_contact_department = models.CharField(max_length=50,null=True,blank=True)
	sec_contact_phone_number = models.CharField(max_length=50, null=True, blank=True)
	sec_contact_email = models.EmailField(max_length=50,null=True,blank=True)
	sec_user_acc = models.ForeignKey(User, null=True, blank=True)
	sec_contact_address_1 = models.CharField(max_length=20,null=True,blank=True)
	sec_contact_created_on = models.DateTimeField(default=timezone.now)
	deleted = models.BooleanField(default=False)


	class Meta:
	    verbose_name_plural = 'Secondary Contact'
	    ordering = ['-sec_user_acc']
	    
	def __unicode__(self):
	    return '%s' %(self.sec_user_acc)


class Quotation(models.Model):
	user_acct = models.ForeignKey(UserAccount, null=True, blank=True)
	item = models.CharField(max_length=20,null=True,blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	price_per_item = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
	total_cost = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
	notes_on_job = models.TextField(null=True,blank=True)
	created_on = models.DateTimeField(default=timezone.now)
	deleted = models.BooleanField(default=False)

	class Meta:
	    verbose_name_plural = 'Quotation'
	    ordering = ['-user_acct']
	    
	def __unicode__(self):
	    return '%s' %(self.user_acc)


class Status(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	alias = models.CharField(max_length=100,null=True,blank=True)

	class Meta:
	    verbose_name_plural = 'Statuses'
	    ordering = ['-name']
	    
	def __unicode__(self):
	    return '%s' %(self.name)


class JobModes(models.Model):
	name = models.CharField(max_length=20,null=True,blank=True)

	class Meta:
	    verbose_name_plural = 'Job Modes'
	    ordering = ['-name']
	    
	def __unicode__(self):
	    return '%s' %(self.name)


class PackageDimension(models.Model):
    box_length      = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
    box_width       = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
    box_height      = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
    box_weight      = models.DecimalField(max_digits = 15, decimal_places = 1, default = 0, null=True, blank=True)
    box_weight_K    = models.DecimalField(max_digits = 15, decimal_places = 1, default = 0, null=True, blank=True)

    class Meta():
        abstract = True


class Batch(models.Model):
	batch_id = models.CharField(max_length=20,null=True,blank=True)
	no_of_jobs = models.IntegerField(null=True,blank=True)
	mode_of_batch = models.CharField(max_length=20,null=True,blank=True)
	deleted = models.BooleanField(default=False)
	created_on = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name_plural = 'Batch'
	    ordering = ['-created_on']
	    
	def __unicode__(self):
	    return '%s' %(self.batch_id)


class Job(PackageDimension):

	job_user_acc = models.ForeignKey(UserAccount, null=True, blank=True)
	job_origin = models.CharField(max_length=50, null=True, blank=True)
	job_destination = models.CharField(max_length=50, null=True, blank=True)
	job_start_date = models.DateField(null=True, blank=True)
	job_end_date = models.DateField(null=True, blank=True)
	job_date_of_arrival = models.DateField(null=True, blank=True)
	job_status = models.CharField(max_length=50, null=True, blank=True)
	job_shipper = models.CharField(max_length=20,null=True,blank=True)
	job_id = models.CharField(max_length=20,null=True,blank=True)
	job_name = models.CharField(max_length=20,null=True,blank=True)
	job_vessel_name = models.CharField(max_length=20,null=True,blank=True)
	job_awl_number = models.CharField(max_length=20,null=True,blank=True)
	job_bol_number = models.CharField(max_length=20,null=True,blank=True)
	job_type = models.CharField(max_length=20,null=True,blank=True)
	batch_type = models.ForeignKey(Batch, null=True, blank=True)

	job_doc_1 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_2 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_3 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_4 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_5 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_6 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_7 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_8 = models.ImageField(upload_to="item_photo", null=True, blank=True)

	job_created_on = models.DateTimeField(default=timezone.now)


	job_in_transit = models.BooleanField(default=False)
	job_arrived = models.BooleanField(default=False)
	job_undergoing_clearnace = models.BooleanField(default=False)
	job_undergoing_ammendment = models.BooleanField(default=False)
	job_examined = models.BooleanField(default=False)
	job_cleared = models.BooleanField(default=False)
	job_completed = models.BooleanField(default=False)
	job_invoiced = models.BooleanField(default=False)
	job_paid_for = models.BooleanField(default=False)
	job_processing = models.BooleanField(default=False)
	job_issue_resolution = models.BooleanField(default=False)


	job_paid = models.CharField(max_length=20,null=True,blank=True)
	job_cost = models.FloatField(default=1.0,null=True, blank=True)
	job_amount_paid = models.FloatField(default=1.0,null=True, blank=True)
	job_amount_balance = models.FloatField(default=1.0,null=True, blank=True)
	insured = models.BooleanField(default=False)
	vat = models.BooleanField(default=False)
	demurrage = models.BooleanField(default=False)
	insurance_charge = models.FloatField(default=0, null=True, blank=True)
	VAT_charge = models.FloatField(default=0, null=True, blank=True)
	demurrage_rate = models.FloatField(max_length=10, default=0.10, null=True, blank=True)
	demurrage_grace_period = models.IntegerField(default=7, null=True, blank=True)
	demurrage_start_date = models.DateField(null=True, blank=True)
	demurrage_end_date = models.DateField(null=True, blank=True)


	shippers_name = models.CharField(max_length=100, null=True, blank=True)
	shippers_address = models.CharField(max_length=100, null=True, blank=True)
	shippers_number = models.IntegerField(null=True, blank=True)
	shippers_acct_no = models.CharField(max_length=100, null=True, blank=True)
	consignees_name = models.CharField(max_length=100, null=True, blank=True)
	consignees_address = models.CharField(max_length=100, null=True, blank=True)
	consignees_number = models.IntegerField(null=True, blank=True)
	consignees_acct_no = models.CharField(max_length=100, null=True, blank=True)
	carrier_agent_name = models.CharField(max_length=100, null=True, blank=True)
	carrier_agent_country = models.CharField(max_length=100, null=True, blank=True)
	carrier_agent_iata_code = models.CharField(max_length=100, null=True, blank=True)
	carrier_agent_acct_no = models.CharField(max_length=100,null=True, blank=True)
	carrier_name = models.CharField(max_length=100, null=True, blank=True)

	
	value_for_carriage = models.CharField(max_length=100, null=True, blank=True)
	number_of_pieces_to_ship = models.IntegerField(null=True, blank=True)
	gross_weight = models.DecimalField(max_digits=15, decimal_places=1, default=0.0, null=True, blank=True)
	box_weight_Actual = models.DecimalField(max_digits=15, decimal_places=1, default=0.0, null=True, blank=True)
	chargeable_rate = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)	
	nature_of_goods = models.CharField(max_length=200, null=True, blank=True)
	quantity_of_goods = models.CharField(max_length=200, null=True, blank=True)
	airline_tracking_number = models.CharField(max_length=100,null=True, blank=True)
	other_charges_due_carrier = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	place_of_execution = models.CharField(max_length=100, null=True, blank=True)


	handling_info = models.TextField(max_length=100, null=True, blank=True)
	job_description = models.TextField(null=True,blank=True)
	job_comment = models.TextField(null=True,blank=True)
	note_on_the_package = models.TextField(max_length=200, null=True, blank=True)
	

	deleted = models.BooleanField(default=False)

	class Meta:
	    verbose_name_plural = 'Jobs'
	    ordering = ['-job_created_on']
	    
	def __unicode__(self):
	    return '%s' %(self.job_id)


class RelationshipManager(models.Model):
	rm_client = models.ForeignKey(UserAccount, null=True,blank=True)
	rm_name = models.CharField(max_length=20,null=True,blank=True)
	rm_email = models.CharField(max_length=20,null=True,blank=True)
	rm_position = models.CharField(max_length=20,null=True,blank=True)
	rm_alt_email = models.CharField(max_length=20,null=True,blank=True)
	rm_contact_no = models.CharField(max_length=20,null=True,blank=True)
	rm_designation = models.CharField(max_length=20,null=True,blank=True)
	rm_office_address = models.TextField(null=True,blank=True)
	deleted = models.BooleanField(default=False)
	rm_created_on = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name_plural = 'Relationship Managers'
	    ordering = ['-rm_created_on']
	    
	def __unicode__(self):
	    return '%s' %(self.rm_client)


class OfficeUseOnly(models.Model):
	rm_client_obj = models.ForeignKey(UserAccount,null=True,blank=True)
	internal_evaluation= models.TextField(null=True,blank=True)
	mode_of_operation= models.CharField(max_length=20,null=True,blank=True)
	special_request= models.CharField(max_length=20,null=True,blank=True)
	staff_evaluation= models.TextField(null=True,blank=True)
	off_deleted = models.BooleanField(default=False)
	created_on = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name_plural = 'Office Use only'
	    ordering = ['-created_on']
	    
	def __unicode__(self):
	    return '%s' %(self.rm_client_obj.user)


class Comments(models.Model):
	job_message = models.ForeignKey(Job, null=True, blank=True)
	msg = models.TextField(null=True,blank=True)
	msg_created_on = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name_plural = 'Comments'
	    ordering = ['-msg_created_on']
	    
	def __unicode__(self):
	    return '%s - %s' %(self.job_message.job_id)


class DockReceipt(models.Model):
    shipping_package                                = models.ForeignKey(Job, null=True, blank=True)
    tracking_number                   				= models.CharField(max_length=100,null=True, blank=True)
    exporter_name_and_address                       = models.CharField(max_length = 100,null=True, blank=True)
    zip_code                                        = models.CharField(max_length = 100,null=True, blank=True)
    consigned_to                                    = models.CharField(max_length = 100,null=True, blank=True)
    notify_party_name_and_address                   = models.CharField(max_length = 100,null=True, blank=True)
    document_number                                 = models.CharField(max_length = 100,null=True, blank=True)
    bl_or_awb_number                                = models.CharField(max_length = 100,null=True, blank=True)
    export_references                               = models.CharField(max_length = 100,null=True, blank=True)
    forwarding_agent_fmc_no                         = models.CharField(max_length = 100,null=True, blank=True)
    state_and_country_of_origin_or_ftz_number       = models.CharField(max_length = 100,null=True, blank=True)
    domestic_routing                                = models.CharField(max_length = 100,null=True, blank=True)
    loading_pier                                    = models.CharField(max_length = 100,null=True, blank=True)
    type_of_move                                    = models.CharField(max_length = 100,null=True, blank=True)
    containerized                                   = models.BooleanField(default=False)
    precarriage_by                                  = models.CharField(max_length = 100,null=True, blank=True)
    place_of_receipt_by_precarrier                  = models.CharField(max_length = 100,null=True, blank=True)
    exporting_carrier                               = models.CharField(max_length = 100,null=True, blank=True)
    port_of_loading                                 = models.CharField(max_length = 100,null=True, blank=True)
    foreign_port_of_unloading                       = models.CharField(max_length = 100,null=True, blank=True)
    place_of_delivery_by_oncarrier                  = models.CharField(max_length = 100,null=True, blank=True)
    mks_nos                                         = models.CharField(max_length = 100,null=True, blank=True)
    no_of_pkgs                                      = models.IntegerField(null=True, blank=True)
    description_of_package_and_goods                = models.CharField(max_length = 100,null=True, blank=True)
    gross_weight                                    = models.IntegerField(null=True, blank=True)
    measurement                                     = models.CharField(max_length=100, null=True, blank=True)
    lighter_truck                                   = models.CharField(max_length = 100,null=True, blank=True)
    arrived_date                                    = models.CharField(max_length = 100,null=True, blank=True)
    arrived_time                                    = models.CharField(max_length = 100,null=True, blank=True)
    created_on                                      = models.DateField(default = timezone.now)
    created_by                                      = models.CharField(max_length = 100,null=True, blank=True)
    batch                                           = models.CharField(max_length = 100,null=True, blank=True)
    unloaded_date                                   = models.CharField(max_length = 100,null=True, blank=True)
    unloaded_time                                   = models.CharField(max_length = 100,null=True, blank=True)
    checked_by                                      = models.CharField(max_length = 100,null=True, blank=True)
    placed_location                                 = models.CharField(max_length = 100,null=True, blank=True)
    receiving_clerk_name                            = models.CharField(max_length = 100,null=True, blank=True)
    date_from_receiving_clerk                       = models.CharField(max_length = 100,null=True, blank=True)



