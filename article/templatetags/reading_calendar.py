#!/usr/bin/env python
# coding: utf-8

from calendar import HTMLCalendar
from django import template
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape


