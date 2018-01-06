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
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB


def check_csrf(request):
    reason = CsrfViewMiddleware().process_view(request, None, (), {})
    if reason:
        return False
    return True


class PostView(View):

    def post(self, request, *args, **kwargs):
        if check_csrf(request) == False:
            return JsonResponse({"error": 1})
        if request.user.is_anonymous() is True:
            return JsonResponse({"error": 1})
        data = json.loads(self.request.body.decode('utf-8'))
        if request.user.is_superuser is True:
            msg = data['message']
        else:
            msg = strip_tags(data['message'])
        user = request.user
        username = user.username
        err = process_message(user, username, msg)
        if err is not None:
            return JsonResponse({"error": 1})
        return JsonResponse({"error": 0})


class ChatView(TemplateView):
    template_name = 'rechat/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous() is True:
            raise(Http404)
        return super(ChatView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        if USE_CACHE is True:
            store = redis.StrictRedis(
                host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            key = SITE_SLUG + '_rechat'
            # retrieve cache history
            data = store.lrange(key, 0, -1)
            context["cache_history"] = reversed(data)
        context["base_template"] = TEMPLATE
        return context
