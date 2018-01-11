# -*- coding: utf-8 -*-
from django.urls.base import reverse
from django.db.models import signals
from instant.models import Channel
from .models import ChatRoom


def room_save(sender, instance, created, **kwargs):
    if created is True:
        paths = reverse("rechat-room", kwargs=dict(room=instance.slug))
        role = "users"
        if instance.groups.all() is not None:
            role = "groups"
        channel, _ = Channel.objects.get_or_create(
            slug=instance.slug, paths=paths, role=role)
        instance.channel = channel
        signals.post_save.disconnect(room_save, sender=ChatRoom)
        instance.save()
        signals.post_save.connect(room_save, sender=ChatRoom)
