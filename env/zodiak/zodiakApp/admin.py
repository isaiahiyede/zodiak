from __future__ import unicode_literals

from django.contrib import admin
from zodiakApp.models import UserAccount, Status, Job, Address, Comments



# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','created_on','phone_number','profile_updated',)
    search_fields = ['created_on','phone_number','profile_updated', ]

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_origin','job_destination')
    search_fields = ['job_origin','job_destination',]

class AddressAdmin(admin.ModelAdmin):
    list_display = ('city','state',)
    search_fields = ['city','state',]

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('job_message',)


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Comments, CommentsAdmin)

