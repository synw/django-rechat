# -*- coding: utf-8 -*

from django.conf import settings
from changefeed.conf import SITE_SLUG


REDIS_HOST = getattr(settings, 'RECHAT_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'RECHAT_REDIS_PORT', 6379)
REDIS_DB = getattr(settings, 'RECHAT_REDIS_DB', 0)

DEFAULT_DB = getattr(settings, 'RECHAT_DEFAULT_DB', SITE_SLUG)
DEFAULT_TABLE = getattr(settings, 'RECHAT_DEFAULT_TABLE', "chat")

USE_CACHE = getattr(settings, 'RECHAT_USE_CACHE', True)
CHAT_CACHE = getattr(settings, 'RECHAT_CACHE', 30)
ttl = 60*60*12
CHAT_CACHE_TTL = getattr(settings, 'RECHAT_CACHE_TTL', ttl)

USE_HISTORY = getattr(settings, 'RECHAT_USE_HISTORY', False)

USE_STATS = getattr(settings, 'RECHAT_USE_STATS', False)

ALLOW_ANONYMOUS = getattr(settings, 'RECHAT_ALLOW_ANONYMOUS', True)