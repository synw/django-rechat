# -*- coding: utf-8 -*-

import datetime
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag()
def get_cache_history(cache_history):
    html = ""
    for key in cache_history:
        s = key.split(':')
        timestamp = datetime.datetime.fromtimestamp(float(s[0])).strftime('%H:%M')
        username = s[1]
        message = s[2].replace("'",'"')
        html += '<a name="'+timestamp+'"></a>'+timestamp+' '+'<strong>'+username+'</strong>'+': '+message+'<br />'
    return mark_safe(html)