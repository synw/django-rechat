import json
from django.middleware.csrf import CsrfViewMiddleware
from django.views import View
from django.http.response import Http404
from django.http import JsonResponse
from django.utils.html import strip_tags
from instant.conf import SITE_SLUG
from rechat.producers import process_message
from rechat.conf import USE_CACHE, TEMPLATE
from django.views.generic.base import TemplateView
from mqueue.models import MEvent
from .models import ChatMessage, ChatRoom
from django.utils import timezone
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB


def check_csrf(request):
    reason = CsrfViewMiddleware().process_view(request, None, (), {})
    if reason:
        return False
    return True


def is_authorized(room, user):
    if room.public is True:
        return True
    if user.is_superuser is True:
        return True
    groups = room.groups.all()
    for group in groups:
        if group in user.groups.all():
            return True
    return False


class PostView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous is True:
            MEvent.objects.create("Anonymous chat post atempt", event_class="Unauthorized",
                                  model=ChatMessage, request=request)
            return JsonResponse({"error": 1})
        return super(PostView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if check_csrf(request) == False:
            return JsonResponse({"error": 403})
        if request.user.is_anonymous is True:
            return JsonResponse({"error": 403})
        try:
            room = ChatRoom.objects.get(slug=kwargs["room"])
        except ChatRoom.DoesNotExist:
            return JsonResponse({"error": 404})
        if is_authorized(room, request.user) is False:
            return JsonResponse({"error": 403})
        data = json.loads(self.request.body.decode('utf-8'))
        if request.user.is_superuser is True:
            msg = data['message']
        else:
            msg = strip_tags(data['message'])
        if msg == "":
            return JsonResponse({"error": 204})
        user = request.user
        username = user.username
        err = process_message(room, username, msg)
        if err is not None:
            return JsonResponse({"error": 500})
        # fire an event
        data["user"] = request.user
        data["date"] = timezone.now()
        MEvent.objects.create(name=msg, event_class="__chat_msg__",
                              model=ChatMessage, data=data)
        return JsonResponse({"error": 0})


class RoomsListView(TemplateView):
    template_name = 'rechat/rooms.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous is True:
            MEvent.objects.create("Anonymous chat rooms list view atempt",
                                  event_class="Unauthorized", model=ChatMessage,
                                  request=request)
            raise(Http404)
        return super(RoomsListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RoomsListView, self).get_context_data(**kwargs)
        rooms = ChatRoom.objects.prefetch_related("groups")
        authorized_rooms = []
        user_groups = self.request.user.groups.all()
        for room in rooms:
            if room.public is True:
                authorized_rooms.append(room)
                continue
            if self.request.user.is_superuser is True:
                authorized_rooms.append(room)
                continue
            groups = room.groups.all()
            for group in groups:
                if group in user_groups:
                    authorized_rooms.append(room)
        context["rooms"] = authorized_rooms
        context["base_template"] = TEMPLATE
        return context


class ChatView(TemplateView):
    template_name = 'rechat/room.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous is True:
            MEvent.objects.create("Anonymous chat view atempt",
                                  event_class="Unauthorized", model=ChatMessage,
                                  request=request)
            raise(Http404)
        return super(ChatView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        # get room
        room_name = kwargs["room"]
        context["not_found"] = False
        room = None
        try:
            room = ChatRoom.objects.get(slug=room_name)
            context["room"] = room
        except ChatRoom.DoesNotExist:
            context["not_found"] = True
        if room is not None:
            if is_authorized(room, self.request.user) is False:
                raise Http404()
            # get cache data
            if USE_CACHE is True:
                store = redis.StrictRedis(
                    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

                key = 'rechat_' + room.slug
                # retrieve cache history
                data = store.lrange(key, 0, -1)
                context["cache_history"] = reversed(data)
        context["base_template"] = TEMPLATE
        return context
