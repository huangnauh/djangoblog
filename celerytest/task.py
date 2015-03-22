#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import

from celery.decorators import task

@task(name="django_blog.celerytest.add")
def add(x,y):
    return x+y
