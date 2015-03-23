#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns,url
from address.views import AddressList

urlpatterns = patterns('',
        url(r'^$',AddressList.as_view()),
        url(r"^upload/$",'address.views.upload'),
        url(r'^contact/$','address.sendMail.contact'),
        url(r'^contact/thanks/$','address.sendMail.contact_thanks'),
        url(r"^longwork/$","address.sendMail.longwork"),
        url(r"^accounts/login/$","address.views.login"),
        )
