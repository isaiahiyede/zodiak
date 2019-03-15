from django import template
from django.template.defaultfilters import stringfilter
from zodiakApp.models import UserAccount, Job, Batch
from django.contrib.auth.models import User
import datetime
from itertools import chain
from operator import attrgetter
from datetime import date, time
from django.utils import timezone

register = template.Library()

@register.simple_tag
def current_year():
    return date.today().year


@register.simple_tag
def getJobCount(request, mode):
	if request.user.is_staff:
		return Job.objects.filter(job_type=mode,deleted=False).count()
	return Job.objects.filter(job_user_acc=request.user.useraccount,job_type=mode,deleted=False).count()


@register.simple_tag
def getBatchCount(request):
	return Batch.objects.filter(deleted=False).count()


@register.simple_tag
def getMessageCount(request):
	if request.user.is_staff:
		return Job.objects.filter(job_new_comment=True,deleted=False).count()
	else:
		return Job.objects.filter(job_new_comment=False,deleted=False,job_user_acc=request.user.useraccount,job_commented_on=True).count()


@register.filter
def get_fields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]
	

    

