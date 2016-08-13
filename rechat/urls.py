# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from rechat.views import ChatView


urlpatterns = patterns('',
    url(r'^', ChatView.as_view(), name="rechat-index"),
)
