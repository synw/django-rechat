from django.views import View
from django.http import HttpRequest
from django.http.response import (
    Http404,
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseBadRequest,
)
from django.utils.html import strip_tags
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ChatRoom
from .producers import process_message


def is_authorized(room, user, groups):
    if user.is_superuser is True:
        return True
    if room.level == "public":
        return True
    elif room.level == "user":
        # print("Public")
        if user.is_authenticated() is True:
            # print("Auth")
            return True
    elif room.level == "groups":
        for group in groups:
            if group in groups:
                return True
    elif room.level == "staff":
        if user.is_staff() is True:
            return True
    return False


class PostView(View, LoginRequiredMixin):
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_anonymous is True:
            return HttpResponseForbidden()
        try:
            room = ChatRoom.objects.get(slug=kwargs["room"])
        except ChatRoom.DoesNotExist:
            return Http404()
        groups = None
        if room.groups.all() is not None:
            groups = self.request.user.groups.all()
        if is_authorized(room, request.user, groups) is False:
            return HttpResponseForbidden()
        # decode data
        _msg = request.POST["msg"]
        # process data
        if request.user.is_superuser is True:
            msg = _msg
        else:
            msg = strip_tags(_msg)
        if msg == "":
            return HttpResponseBadRequest("empty message")
        # publish the message
        process_message(room, request.user, msg)
        return HttpResponse(status=204)


class RoomsListView(TemplateView, LoginRequiredMixin):
    template_name = "rechat/rooms.html"

    def get_context_data(self, **kwargs) -> HttpResponse:
        context = super(RoomsListView, self).get_context_data(**kwargs)
        rooms = ChatRoom.objects.prefetch_related("groups")
        authorized_rooms = []
        groups = None
        for room in rooms:
            if room.groups.all() is not None:
                groups = self.request.user.groups.all()
                break
        for room in rooms:
            if is_authorized(room, self.request.user, groups):
                authorized_rooms.append(room)
        context["rooms"] = authorized_rooms
        return context


class ChatIndexView(TemplateView, LoginRequiredMixin):
    template_name = "rechat/index.html"


class ChatView(TemplateView, LoginRequiredMixin):
    template_name = "rechat/room.html"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        # get room
        room_name = kwargs["room"]
        room = None
        try:
            room = ChatRoom.objects.get(slug=room_name)
            context["room"] = room
        except ChatRoom.DoesNotExist:
            return Http404()
        if room is not None:
            groups = None
            if room.groups.all() is not None:
                groups = self.request.user.groups.all()
            if is_authorized(room, self.request.user, groups) is False:
                raise HttpResponseForbidden()
        return context
