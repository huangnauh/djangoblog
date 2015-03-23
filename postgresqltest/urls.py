#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns,url

urlpatterns = patterns("",
        url(r"^createorder/$",'postgresqltest.views.create_order'),
        url(r"^showorder/(?P<order_id>\d+)$",'postgresqltest.views.show_order'),
        url(r"^showorderall/$",'postgresqltest.views.show_order_all'),
        )
