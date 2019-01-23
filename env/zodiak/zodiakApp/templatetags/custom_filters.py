from django import template
from django.template.defaultfilters import stringfilter
from zodiakApp.models import UserAccount, Job
from django.contrib.auth.models import User
# from export.models import *
import datetime
# import time
from itertools import chain
from operator import attrgetter
# from datetime import datetime
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

    

