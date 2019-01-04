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
    created_on = models.DateTimeField(default=timezone.now)
    user_passport = models.FileField(upload_to="item_photo", null=True, blank=True)
    user_cac = models.FileField(upload_to="item_photo", null=True, blank=True)
    inputter = models.BooleanField(default=True)
    authorizer = models.BooleanField(default=False)
    rm_updated = models.BooleanField(default=False)
    reporter = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
	    verbose_name_plural = 'UserAccount'
	    ordering = ['-created_on']
	    
    def __unicode__(self):
	    return '%s' %(self.user)


class Address(models.Model):
	user_acc = models.ForeignKey(UserAccount, null=True, blank=True)
	address_1 = models.CharField(max_length=20,null=True,blank=True)
	address_2 = models.CharField(max_length=20,null=True,blank=True)
	city = models.CharField(max_length=20,null=True,blank=True)
	state = models.CharField(max_length=20,null=True,blank=True)
	zip_code = models.CharField(max_length=20,null=True,blank=True)

	class Meta:
	    verbose_name_plural = 'Addresses'
	    ordering = ['-user_acc']
	    
	def __unicode__(self):
	    return '%s' %(self.user_acc)


class Status(models.Model):
	name = models.CharField(max_length=20,null=True,blank=True)

	class Meta:
	    verbose_name_plural = 'Status'
	    ordering = ['-name']
	    
	def __unicode__(self):
	    return '%s' %(self.name)


class Job(models.Model):
	job_user_acc = models.ForeignKey(User, null=True, blank=True)
	job_origin = models.CharField(max_length=50, null=True, blank=True)
	job_destination = models.CharField(max_length=50, null=True, blank=True)
	job_start_date = models.DateField(null=True, blank=True)
	job_end_date = models.DateField(null=True, blank=True)
	job_date_of_arrival = models.DateField(null=True, blank=True)
	job_status = models.CharField(max_length=50, null=True, blank=True)
	job_cost = models.FloatField(default=1.0,null=True, blank=True)
	job_amount_paid = models.FloatField(default=1.0,null=True, blank=True)
	job_amount_balance = models.FloatField(default=1.0,null=True, blank=True)
	job_shipper = models.CharField(max_length=20,null=True,blank=True)
	job_description = models.TextField(null=True,blank=True)
	job_comment = models.TextField(null=True,blank=True)
	job_id = models.CharField(max_length=20,null=True,blank=True)
	job_name = models.CharField(max_length=20,null=True,blank=True)
	job_awl_number = models.CharField(max_length=20,null=True,blank=True)
	job_bol_number = models.CharField(max_length=20,null=True,blank=True)
	job_vessel_name = models.CharField(max_length=20,null=True,blank=True)
	job_type = models.CharField(max_length=20,null=True,blank=True)
	job_doc_1 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_2 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_doc_3 = models.ImageField(upload_to="item_photo", null=True, blank=True)
	job_paid_for = models.BooleanField(default=False)
	job_created_on = models.DateTimeField(default=timezone.now)
	deleted = models.BooleanField(default=False)

	class Meta:
	    verbose_name_plural = 'Job'
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
	rm_created_on = models.DateTimeField(default=timezone.now)
	deleted = models.BooleanField(default=False)

	class Meta:
	    verbose_name_plural = 'Relationship Manager'
	    ordering = ['-rm_created_on']
	    
	def __unicode__(self):
	    return '%s' %(self.rm_client)


class Comments(models.Model):
	job_message = models.ForeignKey(Job, null=True, blank=True)
	msg = models.TextField(null=True,blank=True)
	msg_created_on = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name_plural = 'Commnets'
	    ordering = ['-msg_created_on']
	    
	def __unicode__(self):
	    return '%s - %s' %(self.job_message.job_id)

