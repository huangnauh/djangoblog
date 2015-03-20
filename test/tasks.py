#!/usr/bin/env python
# coding: utf-8

from celery import Celery
app = Celery('tasks',broker="amqp://guest@localhost//",backend="amqp")
import time
@app.task
def add(x,y):
    time.sleep(1)
    return  x+y
