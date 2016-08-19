Install
=======

Websockets server
-----------------

Install `Centrifugo <https://github.com/centrifugal/centrifugo/>`_  and 
`Django Instant <https://github.com/synw/django-instant>`_ .

Instructions are `here <http://django-instant.readthedocs.io/en/latest/src/install.html>`_

Add ``'rechat',`` to INSTALLED_APPS and the urls:

.. highlight:: python

::

   url('^chat/', include('rechat.urls')),

Settings
--------

By default only the logged in users can chat. To enable the anonymous users in the chat: in settings.py: 

.. highlight:: python

::

   RECHAT_ALLOW_ANONYMOUS = True
   
You will also have to configure Centrifugo for this: in config.json:

.. highlight:: javascript

::

   {
  "secret": "70b651f6-775a-4949-982b-b387b31c1d84",
  "anonymous": true
  }