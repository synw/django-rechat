History management
==================

Install
-------

The chat messages can be stored in the database. You have to enable it in settings.py

.. highlight:: python

::

   MQUEUE_HOOKS = {
    "rechat": {
        "path": "rechat.hook",
    }
   }

   MQUEUE_NOSAVE = ["ChatMessage"]


How to create a custom hook
---------------------------

Use a `hook.py` file or whatever name with a `save` function that will receive a `MEvent`
object:

::

   def save(event, conf):
    if (event.event_class == "someclass"):
        do_something()
        
The in settings:

::

   MQUEUE_HOOKS = {
    "myhook": {
        "path": "myapp.hook",
    }
   }

   MQUEUE_NOSAVE = ["ChatMessage"]
        
This way it is possible to implement any persistance layer or process for the chat messages.

 