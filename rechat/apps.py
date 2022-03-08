from __future__ import unicode_literals
from django.apps import AppConfig


def connect_signals():
    from django.db.models.signals import post_save
    from .signals import room_save
    from .models import ChatRoom

    post_save.connect(room_save, ChatRoom)


class RechatConfig(AppConfig):
    name = "rechat"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        connect_signals()
