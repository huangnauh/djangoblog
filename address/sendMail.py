#!/usr/bin/env python
# coding: utf-8

from address.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd['email'],
                    ['huanglibo2010@gmail.com',])
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm({'subject': 'I love your site!'})
    return render(request,'address/contact.html',{"form":form},context_instance=RequestContext(request))

def contact_thanks(request):
    return render(request,'address/contact_thanks.html')
