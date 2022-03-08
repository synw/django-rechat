import uuid

from django.db.models import signals
from instant.models import Channel
from .models import ChatRoom


def room_save(sender, instance, created, **kwargs):
    if created is True:
        # generate a channel for the room
        channel_name = instance.slug + "_" + str(uuid.uuid4())[:8]
        channel = Channel.objects.create(name=channel_name)
        groups = instance.groups.all()
        # print("Groups", groups)
        if len(groups) > 0:
            for group in groups:
                channel.groups.add(group)
        channel.save()
        # attach channel to room
        instance.channel = channel
        signals.post_save.disconnect(room_save, sender=ChatRoom)
        instance.save()
        signals.post_save.connect(room_save, sender=ChatRoom)


def room_delete(sender, instance, **kwargs):  # type: ignore
    chan = instance.channel
    instance.channel = None
    instance.save()
    chan.delete()
