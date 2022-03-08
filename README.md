# Django Rechat

Chat application for Django using websockets

## Install

```
pip install django-rechat
```

Add `"rechat"` and `"instant"` to `INSTALLED_APPS` in settings and update `urls.py`:

```python
urlpatterns = [
    # ...
    path("instant/", include("instant.urls")),
    path("rechat/", include("rechat.urls")),
]
```

Install the websockets server: [quickstart](https://github.com/synw/django-instant#install-the-websockets-server)

## Usage

An Alpinejs frontend is available. To use the rechat templates create your own index template
(here with Tailwind css classes):

```django
{% extends "base.html" %}

{% block content %}
{% include "rechat/init.html" %}
<div class="flex flex-row h-full" x-init="$rechat.hxget('{% url 'rechat-rooms' %}', '#rooms')">
  <div id="rooms" class="w-2/12 h-full p-3 border-r border-gray-200 bg-slate-100">
    Loading rooms ..
  </div>
  <div id="room">
    <div class="p-5 text-stone-400">Select a chatroom</div>
  </div>
</div>
{% endblock %}
```

## Todo

- [x] Add a persistence layer option
- [x] Group level authorizations and rooms
- [ ] Rate limits
- [ ] Channel admin, kick/ban
- [ ] Add a presence widget to show users in the chat
