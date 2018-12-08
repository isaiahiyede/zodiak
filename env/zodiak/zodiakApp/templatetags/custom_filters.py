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
def getJobCount(request, status):
    return Job.objects.filter(job_status=status,deleted=False).count()
    

