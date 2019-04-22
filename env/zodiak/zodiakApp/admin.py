from __future__ import unicode_literals

from django.contrib import admin
from zodiakApp.models import UserAccount, Shippers, Documents, ContainerTypes, MiniBatches, Finances, Status, Job, Comments, Batch, RelationshipManager, JobModes, PrimaryContact, SecondaryContact, OfficeUseOnly, Batch



# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','created_on','phone_number','profile_updated',)
    search_fields = ['created_on','phone_number','profile_updated',]

class ContainerTypesAdmin(admin.ModelAdmin):
    list_display = ('job_obj_cont',)
    search_fields = ['job_obj_cont',]

class ShippersAdmin(admin.ModelAdmin):
    list_display = ('shippers_name',)
    search_fields = ['shippers_name',]

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('job_obj_doc',)
    search_fields = ['job_obj_doc',]

class FinancesAdmin(admin.ModelAdmin):
    list_display = ('job_finance',)
    search_fields = ['job_finance',]

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id',)
    search_fields = ['job_id',]

class SecondaryContactAdmin(admin.ModelAdmin):
    list_display = ('sec_contact_name','sec_contact_phone_number',)
    search_fields = ['sec_contact_name','sec_contact_phone_number',]

class PrimaryContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name','contact_phone_number',)
    search_fields = ['contact_name','contact_phone_number',]

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name','alias')
    search_fields = ['name','alias']

class JobModesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('job_message',)

class RelationshipManagerAdmin(admin.ModelAdmin):
    list_display = ('rm_client','rm_email',)

class OfficeUseOnlyAdmin(admin.ModelAdmin):
    list_display = ('rm_client_obj',)

class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_id',)

class MiniBatchesAdmin(admin.ModelAdmin):
    list_display = ('mini_batch_id',)


admin.site.register(Finances, FinancesAdmin)
admin.site.register(Shippers, ShippersAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(ContainerTypes, ContainerTypesAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(MiniBatches, MiniBatchesAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(PrimaryContact, PrimaryContactAdmin)
admin.site.register(SecondaryContact, SecondaryContactAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(JobModes, JobModesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(OfficeUseOnly, OfficeUseOnlyAdmin)
admin.site.register(RelationshipManager, RelationshipManagerAdmin)


