#!/usr/bin/env python
# coding: utf-8

from address.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from .tasks import send_async_email,long_task
import json
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if request.POST['submit'] == "send":
                send_async_email.delay(
                    cd['subject'],
                    cd['message'],
                    cd['email'],
                    ['huanglibo2010@gmail.com',])
            else:
                send_async_email.apply_async([
                    cd['subject'],
                    cd['message'],
                    cd['email'],
                    ['huanglibo2010@gmail.com',]],countdown=60) 
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm({'subject': 'I love your site!'})
    return render(request,'address/contact.html',{"form":form},context_instance=RequestContext(request))

def contact_thanks(request):
    return render(request,'address/contact_thanks.html')

def longwork(request):
    task = long_task.apply_async()
    if task.state == "PENDING":
        response = {
                'state': task.state,
                'current': 0,
                'total': 1,
                'status': 'Pending...'
                }
    elif task.state != "FAILURE":
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return HttpResponse(json.dumps(response))
