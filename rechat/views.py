import json
from django.middleware.csrf import CsrfViewMiddleware
from django.views import View
from django.http import JsonResponse
from django.utils.html import escape
from instant.conf import SITE_SLUG
from rechat.forms import ChatForm
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
        data = json.loads(self.request.body.decode('utf-8'))
        msg = escape(data['message'])
        user = request.user
        username = "anonymous"
        if user.is_authenticated:
            username = user.username
        err = process_message(user, username, msg)
        if err is not None:
            return JsonResponse({"error": 1})
        return JsonResponse({"error": 0})


class ChatView(TemplateView):
    template_name = 'rechat/index.html'

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        if USE_CACHE is True:
            store = redis.StrictRedis(
                host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            key = SITE_SLUG + '_rechat'
            # retrieve cache history
            data = store.lrange(key, 0, -1)
            print(data)
            context["cache_history"] = data
        context["base_template"] = TEMPLATE
        return context
