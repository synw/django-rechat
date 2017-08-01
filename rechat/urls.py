# -*- coding: utf-8 -*-

from django.conf.urls import url
from rechat.views import ChatView, PostView


urlpatterns = [
    url(r'^post$', PostView.as_view(), name="rechat-post"),
    url(r'^', ChatView.as_view(), name="rechat-index"),
]
