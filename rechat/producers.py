# -*- coding: utf-8 -*-
import time
from instant.producers import publish
from instant.conf import SITE_SLUG
from rechat.conf import USE_CACHE, CHANNEL
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CACHE, CHAT_CACHE_TTL


def process_message(user, username, message):
    # 1. handle cache
    if USE_CACHE is True:
        store = redis.StrictRedis(
            host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        # handle cache
        key = SITE_SLUG + '_rechat'
        timestamp = time.time()
        data = str(timestamp) + ':' + username + ':' + message
        store.lpush(key, data)
        print("DATA", store.lrange(key, 0, -1))
        numkeys = store.llen(key)
        if numkeys > CHAT_CACHE:
            num = CHAT_CACHE-1
            store.ltrim(key, 0, -num)
            print("TRIM", store.lrange(key, 0, -1))
        store.expire(key, CHAT_CACHE_TTL)
    # 2. push to socket
    err = publish(message, event_class="__chat_message__",
                  channel=CHANNEL, data={"username": username})
    if err is not None:
        print("Error sending the message:", err)
        raise()
