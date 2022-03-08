from instant.producers import publish

from .models import ChatMessage


def process_message(room, user, message):
    channel = room.channel_name
    bucket = room.name
    # print("Publishing on", channel, "MSG:", message)
    publish(
        channel,
        message,
        event_class="__chat_message__",
        data={"username": user.username},
        bucket=bucket,
    )
    if room.save_messages:
        ChatMessage.objects.create(message=message, room=room, user=user)
