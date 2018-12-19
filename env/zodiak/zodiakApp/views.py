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
from zodiakApp.forms import UserForm, JobForm, UserAccountForm, AddressForm
from zodiakApp.models import Job, UserAccount, Address, Status
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
    print('i got here')
    template_name = 'zodiakApp/adminHome.html'
    context['names'] = User.objects.all()
    context['statuses'] = getStatuses()
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
                return redirect(reverse('zodiakApp:adminPage'))
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


@login_required
def view_jobs(request,jobtype):
    context = {}
    template_name = 'zodiakApp/jobviews.html'
    context['statuses'] = getStatuses()
    context['title'] = jobtype
    context['all_jobs'] = Job.objects.filter(job_status=jobtype, deleted=False)
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


def getStatuses():
    statuses = Status.objects.all()
    return statuses


@login_required
def add_job(request):
    context = {}
    print(randomNumber(10))
    print(request.POST)
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid:
            form2 = form.save(commit=False)
            form2.job_id = randomNumber(10)
            form2.save()
            messages.success(request, 'Job was successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        else:
            print form.errors
            messages.warning(request, 'Job was not successfully created')
            response = redirect(request.META['HTTP_REFERER'])
        return response
    else:
        context['form'] = JobForm()
        context['names'] = User.objects.all()
        context['statuses'] = getStatuses()
        response = render(request, 'zodiakApp/createjob.html', context)
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
        form = JobForm(request.POST,request.FILES,instance=job_obj)
        if form.is_valid:
            print request.POST
            print form.errors
            form.save()
            messages.success(request, 'Job was successfully edited')
            return redirect(reverse('zodiakApp:adminPage'))
        else:
            print form.errors
            messages.warning(request, 'Job was not successfully edited')
            response = redirect(re.META['HTTP_REFERER'])
        return response
    else:
        context['job'] = job_obj
        context['names'] = User.objects.all()
        context['statuses'] = getStatuses()
        response = render(request, 'zodiakApp/editjob.html', context)
        return response


@login_required
def job_view(request,pk):
    context={}
    job_obj = Job.objects.get(pk=pk, deleted=False)
    context['job'] = job_obj
    context['names'] = User.objects.all()
    context['statuses'] = getStatuses()
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

        rp = request.POST
        print(rp)

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
                # print user
                username = user.username

                user_login = authenticate(username=username, password=password)
                UserAccount.objects.create(user=user_login,
                                           profile_updated=True,
                                           phone_number=request.POST.get('phone_number'),
                                           user_passport=request.POST('user_passport'),
                                           user_cac=request.POST('user_cac'))
                # print user_login
                if user_login:
                    # Is the account active? It could have been disabled.
                    if user_login.is_active:
                        # If the account is valid and active, we can log the user in.
                        # We'll send the user back to the homepage.
                        login(request, user_login)
                        messages.success(request, "Sign up was successful")
                        user = request.user
                        return redirect(request.META.get('HTTP_REFERER', '/'))
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
    template_name = 'zodiakApp/adduser.html'
    if request.method = 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request, "User was successful created.")
        else:
            print(userform.errors)
            messages.success(request, "User was not successful created. Try again")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['userform'] = UserForm()
        return render(request,template_name,context)

