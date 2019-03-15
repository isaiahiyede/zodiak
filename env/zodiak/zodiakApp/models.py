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
    comp_name = models.TextField(null=True,blank=True)
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
    staff_account = models.BooleanField(default=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    website = models.CharField(max_length=50,null=True,blank=True)
    cust_type = models.CharField(max_length=50,null=True,blank=True)
    acc_owner = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'User Accounts'
        ordering = ['-created_on']
        
    def __str__(self):
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
        
    def __str__(self):
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
        
    def __str__(self):
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
        
    def __str__(self):
        return '%s' %(self.user_acc)


class Status(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    alias = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ['-name']
        
    def __str__(self):
        return '%s' %(self.name)


class JobModes(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Job Modes'
        ordering = ['-name']
        
    def __str__(self):
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
    status_of_batch = models.CharField(max_length=20,null=True,blank=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    total_batch_cost = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)
    total_batch_weight = models.DecimalField(max_digits = 15, decimal_places = 1, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Batch'

    def getjobs(self):
        return self.job_set.filter(deleted=False)

    def batch_jobs_count(self):
        total = 0
        total = self.job_set.filter(deleted=False,job_type=self.mode_of_batch).count()
        if total == None:
            total = 0
        return total

    def batch_jobs_cost(self):
        total = self.job_set.filter(deleted=False).aggregate(Sum('job_cost'))['job_cost__sum']
        if total == 0.0:
            total = 0.0
        else:
            total = total
        return total

    def batch_weight_total(self):
        total = self.job_set.filter(deleted=False).aggregate(Sum('box_weight_Actual'))['box_weight_Actual__sum']
        if total == 0.0:
            total = 0.0
        else:
            total = total
        return total

    def job_update(self,value):
        if value == "edit":
            batch_jobs = self.job_set.filter(deleted=False)
            for job in batch_jobs:
                job.job_status = self.status_of_batch
                job.save()
        else:
            batch_jobs = self.job_set.filter(deleted=False)
            for job in batch_jobs:
                job.job_status = self.status_of_batch
                job.save()
        return True

    def __str__(self):
        return '%s' %(self.batch_id)




class Job(PackageDimension):
    job_paar = models.BooleanField(default=False) 
    ref_number = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    customer_type = models.CharField(max_length=50, null=True, blank=True) 
    shippers_name = models.CharField(max_length=50, null=True, blank=True)
    shippers_email = models.CharField(max_length=50, null=True, blank=True)
    shippers_number = models.CharField(max_length=50, null=True, blank=True)
    shippers_country = models.CharField(max_length=50, null=True, blank=True)
    shippers_address = models.CharField(max_length=50, null=True, blank=True)
    consignees_name = models.CharField(max_length=50, null=True, blank=True)
    consignees_number = models.CharField(max_length=50, null=True, blank=True)
    consignee_email = models.CharField(max_length=50, null=True, blank=True)
    consignee_country = models.CharField(max_length=50, null=True, blank=True)
    consignees_address = models.CharField(max_length=50, null=True, blank=True)
    country_of_origin = models.CharField(max_length=50, null=True, blank=True)
    country_of_arrival = models.CharField(max_length=50, null=True, blank=True)
    port_of_destination = models.CharField(max_length=50, null=True, blank=True)
    port_of_arrival = models.CharField(max_length=50, null=True, blank=True)
    job_vessel_name = models.CharField(max_length=50, null=True, blank=True)
    job_awl_bol_number = models.CharField(max_length=50, null=True, blank=True)
    paar_date = models.DateField(null=True, blank=True)
    insured = models.BooleanField(default=False)
    insurance_date = models.DateField(null=True, blank=True)
    packing_list = models.BooleanField(default=False)
    packing_list_date = models.CharField(max_length=50, null=True, blank=True)
    job_son = models.BooleanField(default=False)
    son_date = models.DateField(null=True, blank=True)
    job_ccro = models.BooleanField(default=False)
    ccro_date = models.DateField(null=True, blank=True)
    duty_exemption = models.BooleanField(default=False)
    duty_exemption_date = models.DateField(null=True, blank=True)
    batch_type = models.ForeignKey(Batch, null=True, blank=True)

    job_user_acc = models.ForeignKey(UserAccount, null=True, blank=True)
    job_start_date = models.CharField(max_length=200, null=True, blank=True)
    job_end_date = models.CharField(max_length=200, null=True, blank=True)
    job_date_of_arrival = models.CharField(max_length=200, null=True, blank=True)
    job_status = models.CharField(max_length=50, null=True, blank=True)
    job_id = models.CharField(max_length=50,null=True,blank=True)
    job_type = models.CharField(max_length=20,null=True,blank=True)
    job_commented_on = models.BooleanField(default=False)

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

    job_details = models.BooleanField(default=False)
    job_descript = models.BooleanField(default=False)
    job_documentation = models.BooleanField(default=False)
    job_finances = models.BooleanField(default=False)
    job_arr_stat = models.BooleanField(default=False)

    job_paid = models.BooleanField(default=False)
    job_cost = models.FloatField(default=0.0,null=True, blank=True)
    job_amount_paid = models.FloatField(default=1.0,null=True, blank=True)
    job_amount_balance = models.FloatField(default=1.0,null=True, blank=True)
    vat = models.BooleanField(default=False)
    demurrage = models.BooleanField(default=False)
    job_new_comment = models.BooleanField(default=False)

    demurrage_grace_period = models.IntegerField(default=7, null=True, blank=True)
    demurrage_start_date = models.DateField(null=True, blank=True)
    demurrage_end_date = models.DateField(null=True, blank=True)

    number_of_pieces_to_ship = models.IntegerField(null=True, blank=True)
    gross_weight = models.DecimalField(max_digits=15, decimal_places=1, default=0.0, null=True, blank=True)
    box_weight_Actual = models.DecimalField(max_digits=15, decimal_places=1, default=0.0, null=True, blank=True)    
    nature_of_goods = models.CharField(max_length=200, null=True, blank=True)
    quantity_of_goods = models.CharField(max_length=200, null=True, blank=True)
    airline_tracking_number = models.CharField(max_length=100,null=True, blank=True)
    
    place_of_execution = models.CharField(max_length=100, null=True, blank=True)
    no_of_arrival_batches = models.IntegerField(default=0, null=True, blank=True)  

    handling_info = models.TextField(max_length=100, null=True, blank=True)
    job_description = models.TextField(null=True,blank=True)
    job_comment = models.TextField(null=True,blank=True)
    note_on_the_package = models.TextField(max_length=200, null=True, blank=True)
    job_route = models.CharField(max_length=100, null=True, blank=True)

    job_arrival_status = models.BooleanField(default=False)
    job_financial_info = models.BooleanField(default=False)
    job_arrival_status_mode = models.CharField(max_length=100, null=True, blank=True)

    deleted = models.BooleanField(default=False)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Job._meta.fields]


    def jobtotalgrossweight(self):
        total = self.minibatches_set.filter(deleted=False).aggregate(Sum('gross_wgh'))['gross_wgh__sum']
        if total == 0.0:
            total = 0.0
        else:
            total = total
        return total


    def jobtotalnetweight(self):
        total = self.minibatches_set.filter(deleted=False).aggregate(Sum('net_wgh'))['net_wgh__sum']
        if total == 0.0:
            total = 0.0
        else:
            total = total
        return total


    def totalcostofjob(self):
        total = self.finances_set.filter(deleted=False).aggregate(Sum('amount'))['amount__sum']
        if total == 0.0 or total == None:
            total = 0.0
        else:
            total = total
        return total


    def getminibatchesCount(self):
        return self.minibatches_set.filter(deleted=False).count()


    def getcommentsCount(self):
        return self.comments_set.filter(deleted=False).count()


    def getlastcomments(self):
        return self.comments_set.filter(deleted=False)[0]


    def getContainerTypesInfo(self):
        list_of_containers = []
        all_containers = self.containertypes_set.filter(deleted=False)
        if all_containers != []:
            for container in all_containers:
                list_of_containers.append(container.item_info())
        else:
            list_of_containers = "Nil"
        return list_of_containers


    def getDescription(self):
        descriptions = []
        all_desc = self.minibatches_set.filter(deleted=False)
        if all_desc != []:
            for desc in all_desc:
                descriptions.append(desc.item_info())
        else:
            descriptions = "Nil"
        return descriptions


    def getminibatches(self):
        return self.minibatches_set.filter(deleted=False)


    def getcontainertypes(self):
        return self.containertypes_set.filter(deleted=False)


    def getfinances(self):
        return self.finances_set.filter(deleted=False)


    class Meta:
        verbose_name_plural = 'Jobs'
        ordering = ['-job_created_on']

        
    def __str__(self):
        return '%s' %(self.job_id)

class Finances(models.Model):
    job_finance = models.ForeignKey(Job,null=True,blank=True)
    charge_type = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    paid_by = models.CharField(max_length=50, null=True, blank=True)
    date_paid = models.DateField(null=True, blank=True)
    refundablle_as = models.CharField(max_length=50, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)


    def jobtotalCost(self):
        
        total = self.amount
        if total == None or total == 0:
            return 0
        return total


    class Meta:
        verbose_name_plural = 'Finances'
        ordering = ['-created_on']
        
    def __str__(self):
        return '%s' %(self.job_finance)


class MiniBatches(models.Model):
    job = models.ForeignKey(Job,null=True,blank=True)
    no_of_packages = models.IntegerField(null=True, blank=True)
    job_description = models.CharField(max_length=255, null=True, blank=True)
    carrier_name = models.CharField(max_length=50, null=True, blank=True)
    mini_batch_id = models.CharField(max_length=50,null=True, blank=True)
    cbm = models.CharField(max_length=50,null=True, blank=True)
    gross_wgh = models.FloatField(default=0.0, null=True, blank=True)
    net_wgh = models.FloatField(default=0.0, null=True, blank=True)
    exp_date_of_arrival = models.DateField(null=True, blank=True)
    date_of_arrival = models.DateField(null=True, blank=True)
    batch_created_on = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)


    def item_info(self):
        return {'no_of_packages': self.no_of_packages, 'cbm':self.cbm,
                'carrier_name': self.carrier_name, 'job_description':self.job_description,
                'gross_wgh':self.gross_wgh, 'net_wgh': self.net_wgh,
                }

    class Meta:
        verbose_name_plural = 'Mini Batches'
        ordering = ['-batch_created_on']
        
    def __str__unicode__(self):
        return '%s' %(self.mini_batch_id)


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
        
    def __str__(self):
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
        
    def __str__(self):
        return '%s' %(self.rm_client_obj.user)


class ContainerTypes(models.Model):
    job_obj_cont = models.ForeignKey(Job,null=True,blank=True)
    name_of_container = models.CharField(max_length=100,null=True, blank=True)
    number_of_container = models.CharField(max_length=100,null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def item_info(self):
        return {'NAOC': self.name_of_container, 'NUOC': self.number_of_container}

    class Meta:
        verbose_name_plural = 'Types of Containers'
        ordering = ['-created_on']
        
    def __str__(self):
        return '%s' %(self.job_obj_cont)


class Documents(models.Model):
    job_obj_doc = models.ForeignKey(Job,null=True,blank=True)
    name_of_doc = models.CharField(max_length=100,null=True, blank=True)
    doc_obj = models.FileField(upload_to="item_photo", null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Documents'
        ordering = ['-created_on']
        
    def __str__(self):
        return '%s' %(self.job_obj_doc)


class Comments(models.Model):
    job_message = models.ForeignKey(Job, null=True, blank=True)
    msg = models.TextField(null=True,blank=True)
    commented_by = models.CharField(max_length = 255,null=True, blank=True)
    msg_created_on = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-msg_created_on']
        
    def __str__(self):
        return '%s - %s' %(self.job_message.job_id)


class DockReceipt(models.Model):
    shipping_package                                = models.ForeignKey(Job, null=True, blank=True)
    tracking_number                                 = models.CharField(max_length=100,null=True, blank=True)
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



