#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from celery import shared_task,task
from django.core.mail import send_mail
import random
import time

@shared_task
def send_async_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)

@task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ""
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = "{0} {1} {2}...".format(random.choice(verb),
                    random.choice(adjective),random.choice(noun)
                    )
        self.update_state(state="PROGRESS",
                meta={"current":i,"total":total,"status":message
                    })
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
                        'result': 42}

