# -*- coding: utf-8 -*

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

TEMPLATE = getattr(settings, 'RECHAT_TEMPLATE', "rechat/base.html")

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG')
except ImportError:
    raise ImproperlyConfigured(u"Rechat; a SITE_SLUG setting is required")

CHANNEL = getattr(settings, 'RECHAT_CHANNEL', SITE_SLUG + '_chat')

REDIS_HOST = getattr(settings, 'RECHAT_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'RECHAT_REDIS_PORT', 6379)
REDIS_DB = getattr(settings, 'RECHAT_REDIS_DB', 0)

DEFAULT_DB = getattr(settings, 'RECHAT_DEFAULT_DB', SITE_SLUG)
DEFAULT_TABLE = getattr(settings, 'RECHAT_DEFAULT_TABLE', "chat")

USE_CACHE = getattr(settings, 'RECHAT_USE_CACHE', True)
CHAT_CACHE = getattr(settings, 'RECHAT_CACHE', 30)
ttl = 60 * 60 * 12
CHAT_CACHE_TTL = getattr(settings, 'RECHAT_CACHE_TTL', ttl)

USE_HISTORY = getattr(settings, 'RECHAT_USE_HISTORY', False)

USE_STATS = getattr(settings, 'RECHAT_USE_STATS', False)

ALLOW_ANONYMOUS = getattr(settings, 'RECHAT_ALLOW_ANONYMOUS', True)
