from instant.producers import publish


def process_message(room, username, message):
    # push to socket
    channel = "$" + room.slug
    publish(
        channel, message, event_class="__chat_message__", data={"username": username}
    )
