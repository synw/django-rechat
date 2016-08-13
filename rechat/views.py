# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import FormView
from instant.conf import SITE_SLUG
from rechat.forms import ChatForm
from rechat.producers import process_message
from rechat.conf import USE_CACHE
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB


class ChatView(FormView):
    form_class = ChatForm
    template_name = 'rechat/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        if USE_CACHE is True:
            store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            key = SITE_SLUG+'_rechat'
            # retrieve cache history
            data = store.lrange(key, 0, -1)
            context["cache_history"] = data
        return context
    
    def form_valid(self, form):
        message = form.cleaned_data['message']
        username = "anonymous"
        if self.request.user.is_authenticated():
            username = self.request.user.username
        process_message(username, message)
        return super(ChatView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('rechat-index')