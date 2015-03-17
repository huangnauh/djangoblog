#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns,url
from address.views import AddressList

urlpatterns = patterns('',
        url(r'^$',AddressList.as_view()),
        url(r"^upload/$",'address.views.upload'),
        )
