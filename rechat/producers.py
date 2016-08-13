# -*- coding: utf-8 -*-

import time
from django.utils.html import strip_tags
from instant import broadcast
from instant.conf import SITE_SLUG
from rechat.conf import USE_CACHE
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CACHE, CHAT_CACHE_TTL, ALLOW_ANONYMOUS

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
    broadcast_to_socket = False
    if user is None:
        if ALLOW_ANONYMOUS is True:
            broadcast_to_socket = True
    else:
        broadcast_to_socket = True 
    if broadcast_to_socket is True:
        broadcast(message, event_class="__chat_message__", data={"username":username})
    return