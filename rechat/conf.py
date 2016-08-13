# -*- coding: utf-8 -*

from django.conf import settings


REDIS_HOST = getattr(settings, 'RECHAT_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'RECHAT_REDIS_PORT', 6379)
REDIS_DB = getattr(settings, 'RECHAT_REDIS_DB', 0)

USE_CACHE = getattr(settings, 'RECHAT_USE_CACHE', True)
CHAT_CACHE = getattr(settings, 'RECHAT_CACHE', 30)
ttl = 60*60*12
CHAT_CACHE_TTL = getattr(settings, 'RECHAT_CACHE_TTL', ttl)