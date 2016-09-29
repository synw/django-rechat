# -*- coding: utf-8 -*-

from django.conf.urls import url
from rechat.views import ChatView


urlpatterns = [
    url(r'^', ChatView.as_view(), name="rechat-index"),
]
