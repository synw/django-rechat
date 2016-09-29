# -*- coding: utf-8 -*-

import datetime
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG')
except ImportError:
    raise ImproperlyConfigured(u"Rechat; a SITE_SLUG setting is required")

CHANNEL = getattr(settings, 'RECHAT_CHANNEL', SITE_SLUG+'_chat')

register = template.Library()

@register.simple_tag
def get_cache_history(cache_history):
    html = ""
    for key in cache_history:
        s = key.split(':')
        timestamp = datetime.datetime.fromtimestamp(float(s[0])).strftime('%H:%M')
        username = s[1]
        message = s[2]
        html += '<a name="'+timestamp+'"></a>'+timestamp+' '+'<strong>'+username+'</strong>'+': '+message+'<br />'
        html = html.replace("'","\'")
    return mark_safe(html)

@register.simple_tag
def chatchannel():
    return CHANNEL