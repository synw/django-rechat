# -*- coding: utf-8 -*-

from django.conf.urls import url
from rechat.views import ChatView, PostView, RoomsListView


urlpatterns = [
    url(r'^room/(?P<room>.*?)$',
        ChatView.as_view(), name="rechat-room"),
    url(r'^post/(?P<room>.*?)$',
        PostView.as_view(), name="rechat-post"),
    url(r'^', RoomsListView.as_view(), name="rechat-rooms"),
]
