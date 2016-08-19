History management
==================

Install
-------

The chat messages can be stored in Rethinkdb. You have to enable it in settings.py

.. highlight:: python

::

   RECHAT_USE_HISTORY = True
   CHANGEFEED_HANDLERS = ['rechat.r_handlers']
   
Install Rethinkdb, Celery and Django Changefeed: 
`instructions here <http://django-changefeed.readthedocs.io/en/latest/src/install.html>`_

Celery is used to push the documents in Rethinkdb in an asynchronous way.

Why use Rethinkdb for history?
------------------------------

There are 2 main reasons:

- Rethinkdb is good for storing mass amounts of data that do not have many relations between them

- Ability to use the Rethinkdb changefeed: for example to retrieve the chat data from another app 