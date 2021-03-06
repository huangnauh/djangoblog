#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from celery import Celery

broker = "amqp://"
backend = "amqp"
app = Celery('tasks',broker=broker,backend=backend)

@app.task
def add(x,y):
    return x+y
