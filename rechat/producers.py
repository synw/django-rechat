# -*- coding: utf-8 -*-
import time
from instant.producers import publish
from .conf import USE_CACHE
if USE_CACHE is True:
    import redis
    from rechat.conf import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CACHE, CHAT_CACHE_TTL


def process_message(room, username, message):
    # 1. handle cache
    if USE_CACHE is True:
        store = redis.StrictRedis(
            host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        # handle cache
        key = "rechat_"+room.slug
        timestamp = time.time()
        data = str(timestamp) + ':' + username + ':' + message
        store.lpush(key, data)
        numkeys = store.llen(key)
        if numkeys > CHAT_CACHE:
            num = CHAT_CACHE-1
            store.ltrim(key, 0, -num)
        store.expire(key, CHAT_CACHE_TTL)
    # 2. push to socket
    channel = "$"+room.slug
    err = publish(message, event_class="__chat_message__",
                  channel=channel, data={"username": username})
    if err is not None:
        print("Error sending the message:", err)
        raise()
