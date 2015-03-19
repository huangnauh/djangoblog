#!/usr/bin/env python
# coding: utf-8

from django import template
import datetime
register = template.Library()

class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string = format_string
    def render(self,context):
        return datetime.datetime.now().strftime(self.format_string)

@register.tag(name="current_time")
def do_current_time(parser,token):
    try:
        tag_name,format_string = token.split_contents()
    except ValueError:
        raise template.TemplatesSyntaxError(
                "%r tag requires a single arguments" % token.contents.split()[0])
    if format_string[0] == format_string[-1] and format_string[0] in ('"',"'"):
        return CurrentTimeNode(format_string[1:-1]) 
    raise template.TemplatesSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
            )


