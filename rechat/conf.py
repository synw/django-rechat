from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

BASE_TEMPLATE = getattr(settings, "BASE_TEMPLATE", "base.html")

try:
    SITE_SLUG = getattr(settings, "SITE_SLUG")
except ImportError:
    raise ImproperlyConfigured(u"Rechat; a SITE_SLUG setting is required")
