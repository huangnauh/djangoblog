#!/usr/bin/env python
# coding: utf-8

from django import template

register = template.Library()

@register.filter(name="change_gender")
def change_gender(value):
    if value == 'M':
        return '男'
    elif value == 'F':
        return "女"
    else:
        return value

