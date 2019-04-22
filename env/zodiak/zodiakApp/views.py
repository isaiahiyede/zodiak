
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
from zodiakApp.forms import UserForm, DocumentsForm, ContainerTypesForm, StatusRecForm, MiniBatchesForm, BatchProcessForm, FinancialsForm, JobForm, JobForm2, JobForm4, BatchForm, UserAccountForm, PrimaryContactForm, RelationshipManagerForm, QuotationForm, SecondaryContactForm,OfficeUseOnlyForm
from zodiakApp.models import Job, Shippers, Batch, StatusRec, Documents, ContainerTypes, Comments, MiniBatches, Finances, UserAccount, PrimaryContact, Status, RelationshipManager, JobModes, Quotation, SecondaryContact, OfficeUseOnly
from django.core.urlresolvers import reverse
import json
from django.conf import settings
from django.db.models import Sum, Max
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Sum
import csv


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
                    return redirect(reverse('zodiakApp:clientpage'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.warning(request, 'Invalid login details provided')
            return redirect(reverse('zodiakApp:login'))
    else:
        return render(request, 'zodiakApp/login.html', {})


def user_logout(request):
    logout(request)
    return redirect(reverse('zodiakApp:clientpage'))


def jobCount():
    total = Job.objects.filter(deleted=False)
    if total == 0:
        return str(1)
    return str(total.count())


def clientJobCount(name):
    total = Job.objects.filter(deleted=False,job_user_acc=name)
    if total == 0:
        return str(1)
    return str(total.count())


def newMessageCountAdmin():
    return Job.objects.filter(deleted=False,job_new_comment=True).count()


def newMessageCountClient(name):
    return Job.objects.filter(deleted=False,job_new_comment=False,job_user_acc=name).count()


def get_job(request):
    context = {}
    job_pk = request.GET.get('job_id')
    template_name = 'zodiakApp/jobmodal.html'
    job_obj = Job.objects.get(pk=job_pk, deleted=False)
    context['job'] = job_obj
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
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
    context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
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
def reporting(request):
    context = {}
    template_name = 'zodiakApp/reporting.html'
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['all_jobs'] = Job.objects.filter(deleted=False)
    context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
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
def edit_job(request,job_pk):
    context = {}
    template_name = 'zodiakApp/edit_job.html'
    job_obj = Job.objects.get(pk=job_pk, deleted=False)
    context['job_obj'] = job_obj
    response = render(request, template_name, context)
    return response


def randomNumber(value,route,typey,ref,name):
    if route == 'Import':
        val = "IMP"
    else:
        val = "EXP"
    if typey == 'Sea Cargo':
        typey = "SEA"
    elif typey == 'Air Cargo':
        typey = 'AIR'
    elif typey == 'Haulage':
        typey = 'HAU'
    else:
        val = "OTH"
    allowed_chars = ''.join((string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
    while Job.objects.filter(job_id=unique_id):
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))

    return name.user.username[0:3].upper()  +'/'+ ref.upper() +'/'+ clientJobCount(name) +'/'+ typey +'/'+  unique_id +'/'+ val +'/'+ jobCount()


def randomBatchNumber(value):
    allowed_chars = ''.join((string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(9))
    while Batch.objects.filter(batch_id=unique_id):
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(9))
    return '#' + value.upper() + unique_id


def randomMiniBatchNumber():
    allowed_chars = ''.join((string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(9))
    while MiniBatches.objects.filter(mini_batch_id=unique_id):
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(9))
    return '#' + unique_id


def getStatus():
    statuses = Status.objects.all()
    return statuses


def getJobModes():
    jobmodes = JobModes.objects.all()
    return jobmodes


@login_required
def add_job4(request,jobtype):
    context = {}
    print(request.POST)
    job_obj = Job.objects.get(job_id=request.POST.get('job_obj'))
    form = JobForm4(request.POST,instance=job_obj)
    if form.is_valid():
        job_obj.job_arr_stat = True
        job_obj.job_descript = False
        job_obj.job_documentation = False
        job_obj.job_details = False
        job_obj.save()
        form.save()
        context['success'] = 'Job description was successfully submitted...Update Job Arrival Status'
        context['form'] = JobForm()
        context['job_obj'] = request.POST.get('job_obj')
        context['job_obj_obj'] = job_obj
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/createjob.html', context)
        return response
    else:
        print(form.errors)
        messages.warning(request, 'Job was not successfully updated')
        response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def get_user_details(request):
    context = {}
    template_name = 'zodiakApp/customerdetails.html'
    user_obj = User.objects.get(username=request.GET.get('user_obj'))
    useraccount_obj = user_obj.useraccount
    context['user_obj'] = useraccount_obj
    return render(request,template_name,context)


@login_required
def get_shippers_details(request):
    context = {}
    template_name = 'zodiakApp/shippersDetails.html'
    sh_obj = Shippers.objects.get(shippers_name=request.GET.get('shp_obj'))
    context['sh_objs'] = Shippers.objects.all()
    context['sh_obj'] = sh_obj
    return render(request,template_name,context)


@login_required
def add_job(request,jobtype):
    context = {}
    print(request.POST)
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            if request.user.is_staff:
                try:
                    name = UserAccount.objects.get(pk=request.POST.get('job_user_acc'))
                except:
                    name_obj = User.objects.get(username=request.POST.get('job_user_acc'))
                    name = name_obj.useraccount
            else:
                name = request.user.useraccount
            try:
                name_obj = User.objects.get(username=request.POST.get('job_user_acc'))
                name = name_obj.useraccount
                form2.job_user_acc = name
            except:
                try:
                    form2.job_user_acc = UserAccount.objects.get(user=request.user)
                except:
                    print(form.errors)
                    messages.warning(request, 'Job was not successfully created..Please select a customer')
                    response = redirect(request.META['HTTP_REFERER'])
                    return response
            try:
                # job_status = Status.objects.get(name=request.POST.get('job_status'))
                # form2.job_status = job_status.name
                form2.job_status = request.POST.get('job_status')
            except:
                print(form.errors)
                messages.warning(request, 'Job was not successfully created..Please select a Job Status')
                response = redirect(request.META['HTTP_REFERER'])
                return response

            job_type = request.POST.get('job_type')
            if not job_type:
                messages.warning(request, 'Job was not successfully created..Please select a Job Mode')
                response = redirect(request.META['HTTP_REFERER'])
                return response
            # batch_obj = request.POST.get('batch_type')
            # if batch_obj:
            #     batch =  Batch.objects.get(batch_id=batch_obj)
            #     form2.batch_type = batch
            form2.job_id = randomNumber(5,request.POST.get('job_route'),request.POST.get('job_type'),request.POST.get('ref_number'),name)
            form2.save()
            print(form2.job_id)
            messages.success(request, 'Job was successfully created..Please update job arrival status')
            return redirect('zodiakApp:process_job',job_obj=(form2.job_id))
        else:
            print(form.errors)
            messages.warning(request, 'Job was not successfully created')
            context['failed'] = 'failed'
            form = JobForm(request.POST)
            context['form'] = form
            response = render(request, 'zodiakApp/createjob.html', context)
        return response
    else:
        context['form'] = JobForm()
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['sh_objs'] = Shippers.objects.all()
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/createjob.html', context)
        return response


@login_required
def clientpage(request):
    context = {}
    context['messagecount'] = newMessageCountClient(request.user.useraccount)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    user_jobs = Job.objects.filter(job_user_acc=request.user.useraccount, deleted=False)
    context['all_jobs'] = user_jobs
    template_name = 'zodiakApp/clientpage.html'
    response = render(request, template_name, context)
    return response


@login_required
def job_edit(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        print(request.POST)
        try:
            job_obj.job_user_acc = UserAccount.objects.get(pk=request.POST.get('job_user_acc'))
        except:
            user_obj = User.objects.get(username=request.POST.get('job_user_acc'))
            job_obj.job_user_acc = user_obj.useraccount
        job_obj.save()
        form = JobForm(request.POST,request.FILES,instance=job_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            batchNo =request.POST.get('batch_type')
            if batchNo:
                try:
                    job_obj.batch_type = Batch.objects.get(pk=batchNo)
                except:
                    job_obj.batch_type = Batch.objects.get(batch_id=batchNo)
                job_obj.save()
            form2.save()
            messages.success(request, 'Job was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['job'] = job_obj
        context['job_docs'] = Documents.objects.filter(job_obj_doc=job_obj,deleted=False)
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        fin_objs = Finances.objects.filter(deleted=False,job_finance=job_obj)
        doc_objs = Documents.objects.filter(deleted=False,job_obj_doc=job_obj)
        stat_objs = StatusRec.objects.filter(deleted=False,job_stat=job_obj) 
        context['fin_objs'] = fin_objs
        context['doc_objs'] = doc_objs
        context['stat_objs'] = stat_objs
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=job_obj.job_type)
        response = render(request, 'zodiakApp/editjob2.html', context)
        return response


@login_required
def editbatch(request):
    context = {}
    template_name = 'zodiakApp/editminibatch.html'
    if request.method == "POST":
        print(request.POST)
        minibatch_obj = MiniBatches.objects.get(pk=request.POST.get('mini_id'))
        form = MiniBatchesForm(request.POST, instance=minibatch_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job was successfully updated')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        minibatch_obj = MiniBatches.objects.get(pk=request.GET.get('mini_id'))
        context['minibatch_obj'] = minibatch_obj
        response = render(request,template_name,context)
        return response


@login_required
def editOBJ(request):
    identifier = request.POST.get('obj_type')
    obj_id = request.POST.get('obj_id')
    if identifier == 'stat':
        stat_obj = StatusRec.objects.get(pk=obj_id)
        context['stat_obj'] = stat_obj
        template_name = 
    elif identifier == 'doc':
        doc_obj = Documents.objects.get(pk=obj_id)
        context['doc_obj'] = doc_obj
        template_name =
    elif identifier == 'payment':
        fin_obj = Finances.objects.get(pk=obj_id)
        context['fin_obj'] = fin_obj
        template_name =
    response = render(request,template_name,context)
    return response


@login_required
def editContainer(request):
    context = {}
    template_name = 'zodiakApp/editcontainer.html'
    if request.method == "POST":
        print(request.POST)
        cont_obj = ContainerTypes.objects.get(pk=request.POST.get('cont_id'))
        form = ContainerTypesForm(request.POST, instance=cont_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job was successfully updated')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        cont_obj = ContainerTypes.objects.get(pk=request.GET.get('cont_id'))
        context['cont_obj'] = cont_obj
        response = render(request,template_name,context)
        return response


@login_required
def process_job(request,job_obj):
    print(job_obj)
    context={}
    job_obj = Job.objects.get(job_id=job_obj, deleted=False)
    jobtype = job_obj.job_type
    print(request.POST)
    if request.method == "POST":
        types_of_containers = request.POST.getlist('fb_type_of_container')
        number_of_each_containers = request.POST.getlist('fb_number_1')
        if request.POST.get('arrival_status') == "completed":
            if job_obj.job_type == "Sea Cargo":
                fields = ['fb_no_of_packages','fb_no_of_containers','fb_type_of_container','fb_carrier_name','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    job_description=request.POST.get('fb_job_description'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                    )
                minibatch_obj.save()

                for i in types_of_containers:
                    val = types_of_containers.index(i)
                    container_obj = ContainerTypes.objects.create(job_obj_cont=job_obj,name_of_container=i,number_of_container=number_of_each_containers[val])
                    container_obj.save()

                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()

                context['success'] = 'Job arrival status successfully submitted'
                context['job_arrival_status'] = 'job_arrival_status'
                context['form'] = JobForm()
                print('this is the job object i need', request.POST.get('job_obj'))
                context['job_obj'] = request.POST.get('job_obj')
                context['job_obj_obj'] = job_obj
                context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
                context['jobmodes'] = getJobModes()
                context['statuses'] = getStatus()
                context['job_type'] = jobtype
                context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response
            else:
                fields = ['fb_no_of_packages','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    carrier_name=request.POST.get('fb_carrier_name'),
                    job_description=request.POST.get('fb_job_description'),
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )

                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj.save()
                messages.success(request, 'Job arrival status successfully processed...')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response

        else:
            if job_obj.job_type == "Sea Cargo":
                fields = ['fb_no_of_packages','fb_no_of_containers','fb_type_of_container','fb_carrier_name','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm',
                'sb_no_of_packages','sb_no_of_containers','sb_type_of_container','sb_carrier_name','sb_gross_weight','sb_net_weight','sb_exp_date_of_arrival','sb_date_of_arrival','sb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    job_description=request.POST.get('fb_job_description'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('sb_no_of_packages'),
                    carrier_name=request.POST.get('sb_carrier_name'),
                    job_description=request.POST.get('sb_job_description'),
                    gross_wgh=request.POST.get('sb_gross_weight'),
                    net_wgh=request.POST.get('sb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('sb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()

                types_of_containers = request.POST.getlist('fb_type_of_container')
                number_of_each_containers = request.POST.getlist('fb_number_1')

                types_of_containers2 = request.POST.getlist('sb_type_of_container')
                number_of_each_containers2 = request.POST.getlist('sb_number_1')

                for i in types_of_containers:
                    val = types_of_containers.index(i)
                    container_obj = ContainerTypes.objects.create(job_obj_cont=job_obj,name_of_container=i,number_of_container=number_of_each_containers[val])
                    container_obj.save()

                for i in types_of_containers2:
                    val = types_of_containers2.index(i)
                    container_obj = ContainerTypes.objects.create(job_obj_cont=job_obj,name_of_container=i,number_of_container=number_of_each_containers2[val])
                    container_obj.save()


                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                messages.success(request, 'Job arrival status successfully processed...')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response

            else:
                fields = ['fb_no_of_packages','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm',
                    'sb_no_of_packages','sb_gross_weight','sb_net_weight','sb_exp_date_of_arrival','sb_date_of_arrival','sb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    job_description=request.POST.get('fb_job_description'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('sb_no_of_packages'),
                    gross_wgh=request.POST.get('sb_gross_weight'),
                    net_wgh=request.POST.get('sb_net_weight'),
                    carrier_name=request.POST.get('sb_carrier_name'),
                    job_description=request.POST.get('sb_job_description'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('sb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()

                messages.success(request, 'Job arrival status successfully processed...')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response
    else:
        context['job_type'] = jobtype
        context['job_obj'] = job_obj
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/processStep2.html', context)
        return response


@login_required
def process_spec_job(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    jobtype = job_obj.job_type
    print(request.POST)
    if request.method == "POST":
        if request.POST.get('arrival_status') == "completed":
            if job_obj.job_type == "Sea Cargo":
                fields = ['fb_no_of_packages','fb_no_of_containers','fb_type_of_container','fb_carrier_name','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    job_description=request.POST.get('fb_job_description'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                    )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                messages.success(request, 'Job arrival status successfully processed...Next Payment Information')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response
            else:
                fields = ['fb_no_of_packages','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    job_description=request.POST.get('fb_job_description'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )

                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj.save()

                messages.success(request, 'Job arrival status successfully processed...Next Payment Information')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response

        else:
            if job_obj.job_type == "Sea Cargo":
                fields = ['fb_no_of_packages','fb_no_of_containers','fb_type_of_container','fb_carrier_name','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm',
                'sb_no_of_packages','sb_no_of_containers','sb_type_of_container','sb_carrier_name','sb_gross_weight','sb_net_weight','sb_exp_date_of_arrival','sb_date_of_arrival','sb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    job_description=request.POST.get('fb_job_description'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('sb_no_of_packages'),
                    job_description=request.POST.get('sb_job_description'),
                    carrier_name=request.POST.get('sb_carrier_name'),
                    gross_wgh=request.POST.get('sb_gross_weight'),
                    net_wgh=request.POST.get('sb_net_weight'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('sb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()

                messages.success(request, 'Job arrival status successfully processed...Next Payment Information')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response

            else:
                fields = ['fb_no_of_packages','fb_gross_weight','fb_net_weight','fb_exp_date_of_arrival','fb_date_of_arrival','fb_cbm',
                    'sb_no_of_packages','sb_gross_weight','sb_net_weight','sb_exp_date_of_arrival','sb_date_of_arrival','sb_cbm']
                for field in fields:
                    if request.POST.get(field) == "":
                        messages.success(request, 'Job was not successfully processed.Make sure all fields with asteriks are properly filled')
                        response = redirect(request.META['HTTP_REFERER'])
                        return response
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('fb_no_of_packages'),
                    gross_wgh=request.POST.get('fb_gross_weight'),
                    net_wgh=request.POST.get('fb_net_weight'),
                    carrier_name=request.POST.get('fb_carrier_name'),
                    job_description=request.POST.get('fb_job_description'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('fb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('fb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()
                minibatch_obj = MiniBatches.objects.create(
                    no_of_packages=request.POST.get('sb_no_of_packages'),
                    gross_wgh=request.POST.get('sb_gross_weight'),
                    net_wgh=request.POST.get('sb_net_weight'),
                    carrier_name=request.POST.get('sb_carrier_name'),
                    job_decription=request.POST.get('sb_job_description'),
                    #exp_date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_exp_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    #date_of_arrival=datetime.datetime.strptime(request.POST.get('sb_date_of_arrival'),'%m/%d/%Y').strftime('%Y-%m-%d'),
                    cbm=request.POST.get('sb_cbm'),
                    job=job_obj,
                    mini_batch_id=randomMiniBatchNumber()
                )
                minibatch_obj.save()
                job_obj.no_of_arrival_batches += 1
                job_obj.job_arrival_status = True
                job_obj.gross_weight = job_obj.jobtotalgrossweight()
                job_obj.box_weight_Actual = job_obj.jobtotalnetweight()
                job_obj.save()

                messages.success(request, 'Job arrival status successfully processed...Next Payment Information')
                if request.user.is_staff:
                    response = redirect(reverse('zodiakApp:adminPage'))
                else:
                    response = redirect(reverse('zodiakApp:clientpage'))
                return response
    else:
        context['job'] = job_obj
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/processjob.html', context)
        return response


@login_required
def job_view(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    context['job'] = job_obj
    context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=job_obj.job_type)
    response = render(request, 'zodiakApp/viewjob.html', context)
    return response


@login_required
def viewminibatches(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    jobs_minibatches = job_obj.getminibatches()
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['job'] = job_obj
    context['jobs_minibatches'] = jobs_minibatches
    response = response = render(request, 'zodiakApp/minibatch.html', context)
    return response


@login_required
def job_invoice_page(request, pk):
    template = "zodiakApp/job_invoice_email_template.html"
    context = {}
    pkg = get_object_or_404(Job, pk=pk)
    context['pkg'] = pkg
    return render(request, template, context)


@login_required
def statrecords(request):
    context={}
    stat_objs = StatusRec.objects.filter(deleted=False)
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['jobs'] = Job.objects.filter(deleted=False)
    context['stat_objs'] = stat_objs
    response = response = render(request, 'zodiakApp/viewstatrecs.html', context)
    return response


@login_required
def new_stat_info_edit(request,pk):
    context = {}
    stat_obj = StatusRec.objects.get(pk=pk, deleted=False)
    print(request.POST)
    if request.method == "POST":
        form = StatusRecForm(request.POST,instance=stat_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            job_obj = Job.objects.get(job_id=stat_obj.job_stat)
            form2.save()
            job_obj.save()
            messages.warning(request, 'Status was successfully edited')
            response = redirect(reverse('zodiakApp:statrecords'))
        else:
            print(form.errors)
            messages.warning(request, 'Status was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['stat_obj'] = stat_obj
        context['mode_of_batch'] = context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/editstat.html', context)

        return response


@login_required
def get_del_item(request,pk,identifier):
    if identifier == 'mini':
        del_obj = MiniBatches.objects.get(pk=pk,deleted=False)
        del_obj.deleted = True
        del_obj.save()
    else:
        del_obj = ContainerTypes.objects.get(pk=pk,deleted=False)
        del_obj.deleted = True
        del_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response

@login_required
def new_stat(request):
    context = {}
    print(request.POST)
    if request.method == "POST":
        type_of_stat = request.POST.getlist('stat_type')
        job_stat = request.POST.get('job_finance')
        try:
            job_obj = Job.objects.get(job_id=job_stat)
        except:
            job_obj = Job.objects.get(pk=job_stat)

        for i in type_of_stat:
            val = type_of_stat.index(i)
            if StatusRec.objects.filter(deleted=False,stat_type=i).exists():
                continue
            else:
                stat_obj = StatusRec.objects.create(
                    job_stat=job_obj,
                    stat_type=i,
                    )
            stat_obj.save()

        messages.success(request, 'Job payments sucessfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        messages.success(request, 'Oops Something went wrong')
        response = redirect(request.META['HTTP_REFERER'])
        return response


"""" financial """


@login_required
def financerecords(request):
    context={}
    fin_objs = Finances.objects.filter(deleted=False)
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['jobs'] = Job.objects.filter(deleted=False)
    context['fin_objs'] = fin_objs
    response = response = render(request, 'zodiakApp/viewfinances.html', context)
    return response


@login_required
def fin_info_view(request,pk):
    context={}
    fin_obj = Finances.objects.get(deleted=False,pk=pk)
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['fin_obj'] = fin_obj
    response = response = render(request, 'zodiakApp/viewfinances.html', context)
    return response


@login_required
def fin_info_edit(request,pk):
    context = {}
    fin_obj = Finances.objects.get(pk=pk, deleted=False)
    print(request.POST)
    if request.method == "POST":
        form = FinancialsForm(request.POST,instance=fin_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            job_obj = Job.objects.get(job_id=fin_obj.job_finance)
            form2.save()
            job_obj.job_cost = job_obj.totalcostofjob()
            job_obj.save()

            context['success'] = 'Job payment information was successfully updated'
            context['form'] = JobForm()
            context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
            context['jobmodes'] = getJobModes()
            context['statuses'] = getStatus()
            context['job_type'] = jobtype
            context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)

            response = render(request, 'zodiakApp/process.html', context)
        else:
            print(form.errors)
            messages.warning(request, 'Payments was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['form'] = JobForm()
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/processjob.html', context)

        return response


@login_required
def fin_info_delete(request,pk):
    fin_obj = Finances.objects.get(pk=pk, deleted=False)
    fin_obj.deleted = True
    fin_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def stat_info_delete(request,pk):
    stat_obj = StatusRec.objects.get(pk=pk, deleted=False)
    stat_obj.deleted = True
    stat_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def new_financials(request):
    context = {}
    print(request.POST)
    if request.method == "POST":
        type_of_charge = request.POST.getlist('charge_type')
        job_finance = request.POST.get('job_finance')
        try:
            job_obj = Job.objects.get(job_id=job_finance)
        except:
            job_obj = Job.objects.get(pk=job_finance)

        for i in type_of_charge:
            val = type_of_charge.index(i)
            if Finances.objects.filter(deleted=False,charge_type=i).exists():
                continue
            else:
                finance_obj = Finances.objects.create(
                    job_finance=job_obj,
                    charge_type=i,
                    )
            finance_obj.save()

        messages.success(request, 'Job payments sucessfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        messages.success(request, 'Oops Something went wrong')
        response = redirect(request.META['HTTP_REFERER'])
        return response


@login_required
def new_fin_info_edit(request,pk):
    context = {}
    fin_obj = Finances.objects.get(pk=pk, deleted=False)
    print(request.POST)
    if request.method == "POST":
        form = FinancialsForm(request.POST,instance=fin_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            job_obj = Job.objects.get(job_id=fin_obj.job_finance)
            form2.save()
            job_obj.job_cost = job_obj.totalcostofjob()
            job_obj.save()
            messages.warning(request, 'Payments was successfully edited')
            response = redirect(reverse('zodiakApp:financerecords'))
        else:
            print(form.errors)
            messages.warning(request, 'Payments was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['fin_obj'] = fin_obj
        context['form'] = FinancialsForm(instance=fin_obj)
        context['mode_of_batch'] = context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/editpayment.html', context)

        return response


@login_required
def financials(request, job_obj):
    context = {}
    print(request.POST)
    if request.method == "POST":

        type_of_charge = request.POST.getlist('type_of_charge')
        amount = request.POST.getlist('amount')
        date_paid = request.POST.getlist('date_paid')
        refundablle_as = request.POST.getlist('refundablle_as')
        paid_by = request.POST.getlist('paid_by')

        try:
            job_obj = Job.objects.get(job_id=job_obj)
        except:
            job_obj = Job.objects.get(pk=job_obj)

        for i in type_of_charge:
            val = type_of_charge.index(i)
            finance_obj = Finances.objects.create(
                job_finance=job_obj,
                charge_type=i,
                amount=amount[val],
                paid_by=paid_by[val],
                refundablle_as=refundablle_as[val],
                date_paid=date_paid[val]
                )
            finance_obj.save()

        job_obj.job_financial_info = True
        job_obj.job_arr_stat = False
        job_obj.job_cost = job_obj.totalcostofjob()
        job_obj.save()

        messages.success(request, 'Job payments sucessfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response

    else:
        context['form'] = JobForm()
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/processjob.html', context)
        return response


""" finacials ends here """


@login_required
def job_delete(request,pk):
    job_obj = Job.objects.get(pk=pk, deleted=False)
    job_obj.deleted = True
    job_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


def register(request):
    context = {}
    if request.method == "POST":

        rp = request.POST
        print(rp)

        if rp.get('cust_type') == "corporate" and rp.get('comp_name') == "":
            context['form'] = request.POST
            context['message'] = "For corporate accounts, please provide your company name"
            response = render(request, 'zodiakApp/newreg.html', context)
            return response

        form = UserForm(request.POST)
        form2 = UserAccountForm(request.POST)
        form3 = PrimaryContactForm(request.POST)
        form4 = SecondaryContactForm(request.POST)

        if request.POST.get('bot_catcher') != "":
            context['message'] = "iRobot detected...."
            context['form'] = request.POST
            response = render(request, 'zodiakApp/newreg.html', context)
            return response

        if User.objects.filter(username=rp.get('username')).exists() or User.objects.filter(
                email=rp.get('email')).exists():
            context['form'] = request.POST
            context['message'] = """Combination of Username and email already exists. Please enter a
                                      different username and/or email"""
            response = render(request, 'zodiakApp/newreg.html', context)
            return response
        else:
            if form.is_valid():
                user = form.save(commit=False)
                password = rp.get('password')
                password1 = rp.get('password2')
                if password != password1:
                    context['form'] = request.POST
                    context['message'] = "Password mismatch. Try again"
                    response = render(request, 'zodiakApp/newreg.html', context)
                    return response
                if len(password) <= 6:
                    context['form'] = request.POST
                    context['message'] = "Password must be at least 8 characters long"
                    response = render(request, 'zodiakApp/newreg.html', context)
                    return response

                user.set_password(user.password)
                user.date_joined = timezone.now().date()
                user.save()

                user_acc_form = UserAccountForm(request.POST,request.FILES)
                user_acc_form2 = user_acc_form.save(commit=False)
                user_acc_form2.staff_account = False
                try:
                    user_acc_form2.cust_type = request.POST.get('cust_type')
                except:
                    pass
                try:
                    user_acc_form2.comp_name = request.POST.get('comp_name')
                except:
                    pass
                user_acc_form2.save()
                user_primary_contact_form = PrimaryContactForm(request.POST)
                user_secondary_contact_form = SecondaryContactForm(request.POST)

                print(user_acc_form.errors)

                if user_acc_form.is_valid():
                    user_acc_form2 = user_acc_form.save(commit=False)
                    user_acc_form2.user = user
                    user_acc_form2.acc_owner = user.username
                    user_acc_form2.save()

                else:
                    form = UserForm(request.POST)
                    form2 = UserAccountForm(request.POST)
                    form3 = PrimaryContactForm(request.POST)
                    context['form'] = request.POST
                    context['message'] = "Incorrect values submitted...Except for office address and type of business, all others fields should not have spaces in between them"
                    response = render(request, 'zodiakApp/newreg.html', context)
                    return response

                if user_primary_contact_form.is_valid():
                    user_acc_form3 = user_primary_contact_form.save(commit=False)
                    user_acc_form3.user_acc = user
                    user_acc_form3.save()

                    rm_obj = RelationshipManager.objects.create(
                        rm_client=user.useraccount,
                        rm_name=user_acc_form3.contact_name,
                        rm_email=user_acc_form3.contact_email,
                        rm_position=user_acc_form3.contact_position,
                        rm_designation=user_acc_form3.contact_department,
                        rm_office_address=user_acc_form3.contact_address_1,
                        rm_contact_no=user_acc_form3.contact_phone_number
                        )
                    rm_obj.save()

                else:
                    context['form'] = request.POST
                    context['message'] = "Incorrect values submitted...Except for office address, type of business and company name, all others fields should not have spaces in between them"
                    response = render(request, 'zodiakApp/newreg.html', context)
                    return response


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
                    context['form'] = request.POST
                    context['message'] = "Sign up was not successful. Try again"
                    response = render(request, 'zodiakApp/newreg.html', context)
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                ''' try this '''
                # new_user_acc_obj = UserAccount.objects.create(user=user)
            else:
                print(form.errors)
                context['form'] = request.POST
                context['message'] = "Please check and make sure all fields are properly filled"
                response = render(request, 'zodiakApp/newreg.html', context)
                return response
    else:
        context = {}
        response = render(request, 'zodiakApp/newreg.html', context)
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
        if userform.is_valid():
            form = userform.save(commit=False)
            if request.POST['password'] != request.POST['password2']:
                messages.warning(request, "Password mismatch. Try again")
                context['form'] = form
                return render(request,template_name,context)
            else:
                user = User.objects.create(username=form.username, first_name=form.first_name,is_staff=True,
                                            last_name=form.last_name, email=form.email, password=form.password)
                user.save()
                if request.user.is_staff:
                    useraccount = UserAccount.objects.create(user=user,phone_number=request.POST['phone_no'],acc_owner=request.POST['rm_client'])
                else:
                    useraccount = UserAccount.objects.create(user=user,phone_number=request.POST['phone_no'],acc_owner=request.user.username)
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
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        return render(request,template_name,context)


@login_required
def viewusers(request):
    context = {}
    template_name = 'zodiakApp/viewusers.html'
    if request.user.is_staff:
        useraccounts = UserAccount.objects.filter(deleted=False)
    else:
        useraccounts = UserAccount.objects.filter(acc_owner=request.user.username,deleted=False)
    context['users'] = useraccounts
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request,template_name,context)
    return response


""" quotaion starts """


@login_required
def viewquotations(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/viewquotations.html'
    if request.user.is_staff:
        quotations = Quotation.objects.filter(deleted=False)
    else:
        quotations = Quotation.objects.filter(user_acct=request.user.useraccount,deleted=False)
    context['quotations'] = quotations
    response = render(request,template_name,context)
    return response


@login_required
def quote_add(request):
    context = {}
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    print(request.POST)
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            if request.user.is_staff:
                user_obj = User.objects.get(username=request.POST.get('user_acct'))
                form2.user_acct = UserAccount.objects.get(user=user_obj)
            else:
                form2.user_acct = UserAccount.objects.get(user=request.user)
            form2.save()
            messages.success(request, 'Quotation was successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Quotation was not successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        if request.user.is_staff:
            context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        response = render(request, 'zodiakApp/newquotation.html', context)
        return response


@login_required
def add_batch(request):
    context = {}
    context['jobmodes'] = getJobModes()
    print(request.POST)
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.batch_id = randomBatchNumber(request.POST.get('mode_of_batch')[0:3])
            form2.save()
            messages.success(request, 'Batch was successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Batch was not successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        response = render(request, 'zodiakApp/addBatch.html', context)
        return response


@login_required
def viewbatches(request):
    context = {}
    template_name = 'zodiakApp/allbatches.html'
    batches=Batch.objects.filter(deleted=False)
    for batch in batches:
        batch.no_of_jobs = batch.batch_jobs_count()
        batch.total_batch_cost = batch.batch_jobs_cost()
        batch.total_batch_weight = batch.batch_weight_total()
        batch.save()
    context['batches'] = batches
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request,template_name,context)
    return response


@login_required
def print_manifest(request, pk):
    context = {}
    try:
        batch = get_object_or_404(Batch, pk=pk)
    except:
        batch = get_object_or_404(Batch, batch_id=pk)
    packages_assigned_to_batch = Job.objects.filter(batch_type = batch)
    context['batch'] = batch
    context['packages'] = packages_assigned_to_batch
    return render(request, 'zodiakApp/print-manifest.html',context)


@login_required
def batch_delete(request,pk):
    batch_obj = Batch.objects.get(pk=pk, deleted=False)
    batch_obj.deleted = True
    batch_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def batch_info_view(request,pk):
    context={}
    batch_obj = Batch.objects.get(pk=pk, deleted=False)
    batch_jobs = batch_obj.getjobs()
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['batch_obj'] = batch_obj
    context['jobs'] = batch_jobs
    response = response = render(request, 'zodiakApp/batch_info_view.html', context)
    return response


@login_required
def batch_edit(request,pk):
    context={}
    batch_obj = Batch.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        rp = request.POST
        print(rp)
        form = BatchForm(request.POST,request.FILES,instance=batch_obj)
        if form.is_valid():
            form.save()
            batch_obj.job_update('edit')
            messages.success(request, 'Batch was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Batch was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['mode_of_batch'] = context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['batch_obj'] = batch_obj
        response = render(request, 'zodiakApp/editbatch.html', context)
        return response


@login_required
def batch_process(request,pk):
    context={}
    batch_obj = Batch.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        rp = request.POST
        print(rp)
        form = BatchProcessForm(request.POST,request.FILES,instance=batch_obj)
        if form.is_valid():
            form.save()
            batch_obj.job_update('process')
            messages.success(request, 'Batch was successfully processed')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Batch was not successfully processed')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['status_of_batch'] = context['statuses'] = getStatus()
        context['jobmodes'] = getJobModes()
        context['batch_obj'] = batch_obj
        response = render(request, 'zodiakApp/processbatch.html', context)
        return response


@login_required
def quote_delete(request,pk):
    user_obj = Quotation.objects.get(pk=pk, deleted=False)
    user_obj.deleted = True
    user_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def quote_edit(request,pk):
    context={}
    if request.user.is_staff:
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
    quote_obj = Quotation.objects.get(pk=pk, deleted=False)
    if request.method == "POST":
        rp = request.POST
        print(rp)
        form = QuotationForm(request.POST,request.FILES,instance=rm_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quotation was successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            messages.warning(request, 'Quotation was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['quote'] = quote_obj
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/editquotation.html', context)
        return response


@login_required
def quote_view(request,pk):
    context={}
    rm_obj = Quotation.objects.get(pk=pk, deleted=False)
    context['quote'] = quote_obj
    if request.user.is_staff:
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewquotation.html', context)
    return response


""" quotation ends """


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


""" rm starts here """


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
            context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        response = render(request, 'zodiakApp/newrm.html', context)
        return response


@login_required
def add_officeusecase(request,pk):
    rm_obj = UserAccount.objects.get(pk=pk)
    office_use_obj = OfficeUseOnly.objects.create(
        rm_client_obj=rm_obj,
        internal_evaluation = request.POST.get('internal_evaluation'),
        mode_of_operation = request.POST.get('mode_of_operation'),
        special_request = request.POST.get('special_request'),
        staff_evaluation = request.POST.get('staff_evaluation'),
        )

    messages.success(request, 'Successfully created')
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
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    response = render(request, 'zodiakApp/viewrm.html', context)
    return response


@login_required
def rm_edit(request,pk):
    context={}
    if request.user.is_staff:
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
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


""" rm ends here """


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
        try:
            context['officialuse'] = OfficeUseOnly.objects.filter(rm_client_obj=user_obj)
        except:
            pass
        context['useraccount'] = user_obj
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/edituseraccount.html', context)
        return response


@login_required
def user_access(request):
    context={}
    if request.user.is_staff:
        user_obj = UserAccount.objects.filter(deleted=False)
    else:
        user_obj = UserAccount.objects.filter(acc_owner=request.user.username,deleted=False)
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
    if request.user.is_staff:
        context['newmailsCountAdmin'] = Job.objects.filter(job_new_comment=True,deleted=False).count()
        context['newmails'] = Job.objects.filter(deleted=False,job_commented_on=True)
    else:
        context['newmailsCountUser'] = Job.objects.filter(job_new_comment=False,deleted=False,job_user_acc=request.user.useraccount,job_commented_on=True).count()
        context['newmails'] = Job.objects.filter(deleted=False,job_commented_on=True,job_user_acc=request.user.useraccount)
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


@login_required
def adminPage(request):
    context = {}
    context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
    context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    template_name = 'zodiakApp/adminHome.html'
    context['all_jobs'] = Job.objects.filter(deleted=False)
    return render(request, template_name, context)


@login_required
def docrecords(request):
    context={}
    doc_objs = Documents.objects.filter(deleted=False)
    context['mode_of_batch'] = context['jobmodes'] = getJobModes()
    context['statuses'] = getStatus()
    context['jobs'] = Job.objects.filter(deleted=False)
    context['doc_objs'] = doc_objs
    response = response = render(request, 'zodiakApp/viewdocs.html', context)
    return response


@login_required
def addDoc(request, job_obj):
    context = {}

    if request.method == "POST":

        document_type = request.POST.getlist('document_type')
        file_obj = request.FILES.getlist('file_obj')

        try:
            job_obj = Job.objects.get(job_id=job_obj)
        except:
            job_obj = Job.objects.get(pk=job_obj)


        for i in document_type:
            val = document_type.index(i)
            print(i)
            if Documents.objects.get(job_obj_doc=job_obj,name_of_doc=i).exists():
                print(True)
                continue
            else:
                doc_obj = Documents.objects.create(
                    job_obj_doc=job_obj,
                    name_of_doc=i,
                    doc_obj=file_obj[val],
                    )
            doc_obj.save()

        messages.success(request, 'Job documents were sucessfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response

    else:
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/processjob.html', context)
        return response


@login_required
def delete_doc(request, pk):
    doc_obj = Documents.objects.get(pk=pk, deleted=False)
    doc_obj.deleted = True
    doc_obj.save()
    response = redirect(request.META['HTTP_REFERER'])
    return response


@login_required
def new_doc_info_edit(request,pk):
    context = {}
    doc_obj = Documents.objects.get(pk=pk, deleted=False)
    print(request.POST)
    if request.method == "POST":
        form = DocumentsForm(request.POST,request.FILES,instance=doc_obj)
        if form.is_valid():
            form2 = form.save(commit=False)
            job_obj = Job.objects.get(job_id=doc_obj.job_obj_doc)
            form2.save()
            job_obj.save()
            messages.warning(request, 'Document was successfully edited')
            response = redirect(reverse('zodiakApp:docrecords'))
        else:
            print(form.errors)
            messages.warning(request, 'Document was not successfully edited')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['doc_obj'] = doc_obj
        context['form'] = DocumentsForm(instance=doc_obj)
        context['mode_of_batch'] = context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        response = render(request, 'zodiakApp/editdoc.html', context)

        return response


@login_required
def add_new_doc(request):
    context = {}
    print(request.POST)

    if request.method == "POST":

        document_type = request.POST.getlist('document_type')
        # file_obj = request.FILES.getlist('file_obj')
        job_finance = request.POST.get('job_finance')

        try:
            job_obj = Job.objects.get(job_id=job_finance)
        except:
            job_obj = Job.objects.get(pk=job_finance)

        for i in document_type:
            print(i)
            val = document_type.index(i)
            if Documents.objects.filter(deleted=False,job_obj_doc=job_obj,name_of_doc=i).exists():
                continue
            else:
                doc_obj = Documents.objects.create(
                    job_obj_doc=job_obj,
                    name_of_doc=i,
                    )
            doc_obj.save()

        messages.success(request, 'Job documents were sucessfully updated')
        response = redirect(request.META['HTTP_REFERER'])
        return response

    else:
        context['names'] = UserAccount.objects.filter(deleted=False,staff_account=False)
        context['jobmodes'] = getJobModes()
        context['statuses'] = getStatus()
        context['job_type'] = jobtype
        context['batches'] = Batch.objects.filter(deleted=False,mode_of_batch=jobtype)
        response = render(request, 'zodiakApp/processjob.html', context)
        return response


@login_required
def get_job_comments(request):
    context = {}
    print('got here')
    context['comments'] = Comments.objects.filter(job_message=request.GET.get('job_id'))
    context['job'] = request.GET.get('job_id')
    template_name = 'zodiakApp/comment.html'
    return render(request, template_name, context)


@login_required
def get_job_desc(request):
    context = {}
    jobs = Job.objects.get(pk=request.GET.get('job_id'))
    print(jobs.getDescription())
    context['jobs_info'] = jobs.getDescription()
    template_name = 'zodiakApp/descinfo.html'
    return render(request, template_name, context)


@login_required
def get_job_info(request):
    context = {}
    jobs = Job.objects.get(pk=request.GET.get('job_id'))
    context['jobs_info'] = jobs.getContainerTypesInfo()
    template_name = 'zodiakApp/descinfo2.html'
    return render(request, template_name, context)


@login_required
def post_comments(request,pk):
    print(request.POST)
    job_obj = Job.objects.get(pk=pk)
    context = {}
    if request.user.is_staff:
        commenter = 'admin'
        job_obj.job_new_comment = False
    else:
        job_obj.job_new_comment = True
        commenter = request.user.username
    job_obj.job_commented_on = True
    job_obj.save()
    comm_obj = Comments.objects.create(job_message=job_obj,msg=request.POST.get('msg'),commented_by=commenter)
    comm_obj.save()
    messages.success(request, 'Job comments were sucessfully updated')
    response = redirect(request.META['HTTP_REFERER'])
    return response




