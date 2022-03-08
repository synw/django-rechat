from instant.producers import publish


def process_message(room, username, message):
    # push to socket
    channel = room.channel_name
    bucket = room.name
    # print("Publishing on", channel, "MSG:", message)
    publish(
        channel,
        message,
        event_class="__chat_message__",
        data={"username": username},
        bucket=bucket,
    )
