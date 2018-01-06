# -*- coding: utf-8 -*-
from rechat.models import ChatMessage


def save(event, conf):
    if not (event.event_class == "__chat_msg__"):
        return
    ChatMessage.objects.create(message=event.name, date=event.data["date"],
                               user=event.data["user"])
