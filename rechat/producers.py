# -*- coding: utf-8 -*-

import time
from django.utils.html import strip_tags
from instant import broadcast
from instant.conf import SITE_SLUG
from rechat.conf import USE_CACHE, USE_HISTORY, ALLOW_ANONYMOUS
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CACHE, CHAT_CACHE_TTL
if USE_HISTORY:
    from changefeed.tasks import push_to_feed

def process_message(user, username, message):
    message = strip_tags(message)
    store_in_cache = False
    # 1. handle cache
    if USE_CACHE is True:
        # if user is anonymous
        if user is None:
            if ALLOW_ANONYMOUS is True:
                store_in_cache = True
        else:
            store_in_cache = True
    if store_in_cache is True:
        store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        # handle cache
        key = SITE_SLUG+'_rechat'
        timestamp = time.time()
        data = str(timestamp)+':'+username+':'+message
        store.rpush(key, data)
        store.ltrim(key, 0, CHAT_CACHE)
        store.expire(key, CHAT_CACHE_TTL)
    # 2. push to socket
    push = False
    if user is None:
        if ALLOW_ANONYMOUS is True:
            push = True
    else:
        push = True 
    if push is False:
        return
    broadcast(message, event_class="__chat_message__", data={"username":username})
    # 3. manage history
    if USE_HISTORY:
        data = {"message":message, "event_class":"__chat_message__", "username":username}
        push_to_feed(data)
    return