from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def connect_signals():
    from django.db.models.signals import post_save, pre_delete
    from .signals import room_save, room_delete
    from .models import ChatRoom

    post_save.connect(room_save, ChatRoom)
    pre_delete.connect(room_delete, ChatRoom)


class RechatConfig(AppConfig):
    name = "rechat"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        try:
            getattr(settings, "SITE_SLUG")
        except ImportError:
            raise ImproperlyConfigured("Rechat: a SITE_SLUG setting is required")
        connect_signals()
