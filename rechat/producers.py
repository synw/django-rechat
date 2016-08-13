# -*- coding: utf-8 -*-

import time
from django.utils.html import strip_tags
from instant import broadcast
from instant.conf import SITE_SLUG
from rechat.conf import USE_CACHE
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CACHE, CHAT_CACHE_TTL

def process_message(username, message):
    message = strip_tags(message)
    if USE_CACHE is True:
        store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        # handle cache
        key = SITE_SLUG+'_rechat'
        timestamp = time.time()
        data = str(timestamp)+':'+username+':'+message
        store.rpush(key, data)
        store.ltrim(key, 0, CHAT_CACHE)
        store.expire(key, CHAT_CACHE_TTL)
    # push to socket
    broadcast(message, event_class="__chat_message__", data={"username":username})
    return