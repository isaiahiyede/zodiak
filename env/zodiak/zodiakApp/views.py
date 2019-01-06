from __future__ import unicode_literals
from django.template.loader import render_to_string, get_template
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.template.context import RequestContext
from django.template import Context
from django.db.models import Count
from django import template
import random, datetime, string
from zodiakApp.forms import UserForm, JobForm, UserAccountForm, AddressForm, RelationshipManagerForm
from zodiakApp.models import Job, UserAccount, Address, Status, RelationshipManager, JobModes
from django.core.urlresolvers import reverse
import json
from django.conf import settings
from django.db.models import Sum, Max
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Sum
import csv


@login_required
def adminPage(request):
    context = {}
    template_name = 'zodiakApp/adminHome.html'
    context['names'] = UserAccount.objects.filter(deleted=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    # context['jobs'] = Job.objects.all()
    return render(request, template_name, context)


@login_required
def clientPage(request):
    context = {}
    template_name = 'zodiakApp/clientPAGE.html'
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    # context['jobs'] = Job.objects.all()
    return render(request, template_name, context)


def user_login(request):
    if request.method == 'POST':
        print('i got here')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    return redirect(reverse('zodiakApp:adminPage'))
                else:
                    return redirect(reverse('zodiakApp:clientPage'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.warning(request, 'Invalid login details provided')
            return redirect(reverse('zodiakApp:login'))
    else:
        return render(request, 'zodiakApp/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('zodiakApp:adminPage'))



def get_job(request):
    context = {}
    job_pk = request.GET.get('job_id')
    template_name = 'zodiakApp/jobmodal.html'
    job_obj = Job.objects.get(pk=job_pk, deleted=False)
    context['job'] = job_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['names'] = UserAccount.objects.filter(deleted=False)
    response = render(request, template_name, context)
    return response


def get_jobs_selected(request):
    context = {}
    user_obj = request.GET.get('user_obj')
    selected = request.GET.get('selected')
    jobtype = request.GET.get('jobtype')
    job_status = Status.objects.get(alias=selected)
    template_name = 'zodiakApp/tabledata.html'
    if request.user.is_staff:
        job_obj = Job.objects.filter(job_status=job_status.name, job_type=jobtype, deleted=False)
    else:
        job_obj = Job.objects.filter(job_user_acc=request.user.useraccount, job_status=job_status.name, job_type=jobtype, deleted=False) 
        print(job_obj.count())   
    context['all_jobs'] = job_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['names'] = UserAccount.objects.filter(deleted=False)
    response = render(request, template_name, context)
    return response


@login_required
def view_jobs(request,jobtype):
    context = {}
    print(jobtype)
    template_name = 'zodiakApp/jobviews.html'
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['title'] = jobtype
    context['all_jobs'] = Job.objects.filter(job_type=jobtype,deleted=False)
    response = render(request, template_name, context)
    return response


@login_required
def view_user_jobs(request,jobtype):
    context = {}
    template_name = 'zodiakApp/jobviews.html'
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['title'] = jobtype
    context['all_jobs'] = Job.objects.filter(job_user_acc=request.user.useraccount,job_type=jobtype, deleted=False)
    response = render(request, template_name, context)
    return response


@login_required
def edit_job(request, job_pk):
    context = {}
    template_name = 'zodiakApp/edit_job.html'
    job_obj = Job.objects.get(pk=job_pk, deleted=False)
    context['job_obj'] = job_obj
    response = render(request, template_name, context)
    return response


def randomNumber(value):
    allowed_chars = ''.join((string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
    while Job.objects.filter(job_id=unique_id):
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
    return '#' + 'JOB' + unique_id


def getStatus():
    statuses = Status.objects.all()
    return statuses

def getJobModes():
    jobmodes = JobModes.objects.all()
    return jobmodes


@login_required
def add_job(request):
    context = {}
    print(randomNumber(10))
    print(request.POST)
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.job_id = randomNumber(10)
            try:
                form2.job_user_acc = UserAccount.objects.get(pk=request.POST.get('job_user_acc'))
            except:
                form2.job_user_acc = UserAccount.objects.get(user=request.user)
            job_status = Status.objects.get(name=request.POST.get('job_status'))
            form2.job_status = job_status.name
            form2.save()
            messages.success(request, 'Job was successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            print(JobForm())
            messages.warning(request, 'Job was not successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['form'] = JobForm()
        context['names'] = UserAccount.objects.filter(deleted=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/newjob.html', context)
        return response


@login_required
def clientpage(request):
    context = {}
    template_name = 'zodiakApp/clientpage.html'
    user_jobs = Job.objects.filter(job_user_acc=request.user.useraccount, deleted=False)
    context['userjobs'] = user_jobs
    response = render(request, template_name, context)
    return response


@login_required
def job_edit(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        print(request.POST)
        job_obj.job_user_acc = UserAccount.objects.get(pk=request.POST.get('job_user_acc'))
        job_obj.save()
        form = JobForm(request.POST,request.FILES,instance=job_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            messages.success(request, 'Job was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            print(JobForm())
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['job'] = job_obj
        context['names'] = UserAccount.objects.filter(deleted=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/neweditjob.html', context)
        return response


@login_required
def process_job(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        form = JobForm(request.POST,request.FILES,instance=job_obj)
        if form.is_valid():
            print(request.POST)
            print(form.errors)
            form.save()
            messages.success(request, 'Job was successfully edited')
            return redirect(reverse('zodiakApp:adminPage'))
        else:
            print(form.errors)
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(re.META['HTTP_REFERER'])
        return response
    else:
        context['job'] = job_obj
        context['names'] = UserAccount.objects.filter(deleted=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/processjob.html', context)
        return response


@login_required
def job_view(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    context['job'] = job_obj
    context['names'] = UserAccount.objects.filter(deleted=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewjob.html', context)
    return response


@login_required
def job_delete(request,pk):
    job_obj = Job.objects.get(pk=pk, deleted=False)
    job_obj.deleted = True
    job_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


def register(request):
    if request.method == "POST":

        rp = request.POST
        print(rp)

        if request.POST.get('bot_catcher') != "":
            messages.warning(request, "Invalid details provided")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if request.POST.get('phone_number') == "":
            messages.warning(request, "Please provide a valid phone number. Try again")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if request.POST.get('user_passport') == "":
            messages.warning(request, "Please provide a valid passport")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if request.POST.get('user_cac') == "":
            messages.warning(request, "Please provide a valid CAC document")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        form = UserForm(request.POST)

        if User.objects.filter(username=rp.get('username')).exists() or User.objects.filter(
                email=rp.get('email')).exists():
            messages.warning(request, "Combination of Username and email already exists. Please enter a"
                                      " different username and/or email")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            if form.is_valid():
                user = form.save(commit=False)
                password = rp.get('password')
                password1 = rp.get('password2')
                if password != password1:
                    messages.warning(request, "Password mismatch. Try again")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                if len(password) < 6:
                    messages.warning(request, "Password less than six characters in length")
                    return redirect(request.META.get('HTTP_REFERER', '/'))

                user.set_password(user.password)
                user.date_joined = timezone.now().date()
                user.save()
                user_acc_form = UserAccountForm(request.POST,request.FILES)
                print(user_acc_form.errors)

                if user_acc_form.is_valid():
                    user_acc_form2 = user_acc_form.save(commit=False)

                    user_acc_form2.user = user
                    user_acc_form2.save()

                else:
                    messages.warning(request, "Please check and make sure all fields are properly filled")
                    return redirect(request.META.get('HTTP_REFERER', '/'))

                print(user_acc_form)
                user_login = authenticate(username=user.username, password=password)

                # print user_login
                if user_login:
                    # Is the account active? It could have been disabled.
                    if user_login.is_active:
                        # If the account is valid and active, we can log the user in.
                        # We'll send the user back to the homepage.
                        login(request, user_login)
                        messages.success(request, "Sign up was successful")
                        user = request.user
                        return redirect(reverse('zodiakApp:clientpage'))
                else:
                    messages.success(request, "Sign up was not successful. Try again")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                ''' try this '''
                # new_user_acc_obj = UserAccount.objects.create(user=user)
            else:
                print(form.errors)
                messages.success(request, "Sign up was not successful. Try again")
                return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context = {}
        response = render(request, 'zodiakApp/register.html', context)
        return response


@login_required
def addUser(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/adduser.html'
    if request.method == 'POST':
        print(request.POST)
        userform = UserForm(request.POST)
        if userform.is_valid()():
            form = userform.save(commit=False)
            if request.POST['password'] != request.POST['password2']:
                messages.warning(request, "Password mismatch. Try again")
                context['form'] = form
                return render(request,template_name,context)
            else:
                user = User.objects.create(username=form.username, first_name=form.first_name,is_staff=True,
                                            last_name=form.last_name, email=form.email, password=form.password)
                user.save()
                useraccount = UserAccount.objects.create(user=user,phone_number=request.POST['phone_no'])
                useraccount.save()
                messages.success(request, "User was successful created.")
        else:
            print(userform.errors)
            context['form'] = userform
            messages.warning(request, "User was not successful created. Try again")
            return render(request,template_name,context)   
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['userform'] = UserForm()
        return render(request,template_name,context)


@login_required
def viewusers(request):
    context = {}
    template_name = 'zodiakApp/viewusers.html'
    useraccounts = UserAccount.objects.filter(deleted=False)
    context['users'] = useraccounts
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request,template_name,context)
    return response


@login_required
def viewrms(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/viewrms.html'
    if request.user.is_staff:
        rms = RelationshipManager.objects.filter(deleted=False)
    else:
        rms = RelationshipManager.objects.filter(rm_client=request.user.useraccount,deleted=False)
    context['rms'] = rms
    response = render(request,template_name,context)
    return response


@login_required
def add_rm(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    print(request.POST)
    if request.method == "POST":
        form = RelationshipManagerForm(request.POST)
        if form.is_valid():
            print(form.errors)
            form2 = form.save(commit=False)
            if request.user.is_staff:
                user_obj = User.objects.get(username=request.POST.get('rm_client'))
                form2.rm_client = UserAccount.objects.get(user=user_obj)
            else:
                form2.rm_client = UserAccount.objects.get(user=request.user)
            form2.save()
            messages.success(request, 'Rm was successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Rm was not successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        if request.user.is_staff:
            context['names'] = UserAccount.objects.filter(deleted=False)
        response = render(request, 'zodiakApp/newrm.html', context)
        return response


@login_required
def user_view(request,pk):
    context={}
    user_obj = UserAccount.objects.get(pk=pk, deleted=False)
    context['useraccount'] = user_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewuseraccount.html', context)
    return response


@login_required
def user_view_home(request,username):
    context={}
    user_obj = User.objects.get(username=username)
    try:
        context['useraccount'] = UserAccount.objects.get(user=user_obj, deleted=False)
    except:
        context['useraccount'] = user_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewuseraccount.html', context)
    return response


@login_required
def user_delete(request,pk):
    user_obj = UserAccount.objects.get(pk=pk, deleted=False)
    user_obj.deleted = True
    user_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def rm_delete(request,pk):
    user_obj = RelationshipManager.objects.get(pk=pk, deleted=False)
    user_obj.deleted = True
    user_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def rm_view(request,pk):
    context={}
    rm_obj = RelationshipManager.objects.get(pk=pk, deleted=False)
    context['rm'] = rm_obj
    if request.user.is_staff:
        context['names'] = UserAccount.objects.filter(deleted=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewrm.html', context)
    return response


@login_required
def rm_edit(request,pk):
    context={}
    if request.user.is_staff:
        context['names'] = UserAccount.objects.filter(deleted=False)
    rm_obj = RelationshipManager.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        rp = request.POST
        print(rp)
        form = RelationshipManagerForm(request.POST,request.FILES,instance=rm_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'RM was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'RM was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['rm'] = rm_obj
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/editrm.html', context)
        return response


@login_required
def user_edit(request,pk):
    context={}
    user_obj = UserAccount.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        rp = request.POST
        print(rp)
        form = UserAccountForm(request.POST,request.FILES,instance=user_obj)
        if form.is_valid():
            user_obj = User.objects.get(username=rp['username'])
            userform = form.save(commit=False)
            userform.user = user_obj
            if 'inputter' in rp:
                userform.inputter = True
            else:
                userform.inputter = False
            if 'reporter' in rp:
                userform.reporter = True
            else:
                userform.reporter = False
            if 'authorizer' in rp:
                userform.authorizer = True
            else:
                userform.authorizer = False
            if 'administrator' in rp:
                userform.administrator = True
            else:
                userform.administrator = False
            if 'profile_updated' in rp:
                userform.profile_updated = True
            else:
                userform.profile_updated = False
            userform.save()
            messages.success(request, 'UserAccount was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Useraccount was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['useraccount'] = user_obj
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/edituseraccount.html', context)
        return response


@login_required
def user_access(request):
    context={}
    user_obj = UserAccount.objects.filter(deleted=False)
    context['names'] = user_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    if request.method == "POST":
        print('see me')
        rp = request.POST
        the_list = (rp.getlist('acc'))
        user_acc_obj = User.objects.get(username=rp['user_acc'])

        if rp.get('acc_action') == 'Add':
            if 'inputter' in the_list:
                user_acc_obj.useraccount.inputter = True
            if 'administrator' in the_list:
                user_acc_obj.useraccount.administrator = True
            if 'reporter' in the_list:
                print('reporter found')
                user_acc_obj.useraccount.reporter = True
            if 'authorizer' in the_list:
                user_acc_obj.useraccount.authorizer = True
        else:
            if 'inputter' in the_list:
                user_acc_obj.useraccount.inputter = False
            if 'administrator' in the_list:
                user_acc_obj.useraccount.administrator = False
            if 'reporter' in the_list:
                print('reporter found')
                user_acc_obj.useraccount.reporter = False
            if 'authorizer' in the_list:
                user_acc_obj.useraccount.authorizer = False

        user_acc_obj.useraccount.save()
        messages.success(request, 'Useraccount was successfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        response = render(request, 'zodiakApp/useraccess.html', context)
        return response


@login_required
def mails(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/adminmailbox.html'
    return render(request, template_name, context)


@login_required
def newmail(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/newmail.html'
    return render(request, template_name, context)


@login_required
def view_mail(request,pk):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/viewmail.html'
    return render(request, template_name, context)




