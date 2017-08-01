Install
=======

Websockets server
-----------------

Install `Django Instant <https://github.com/synw/django-instant>`_ .

Instructions are `here <http://django-instant.readthedocs.io/en/latest/src/install.html>`_

``pip install redis``

Add ``'rechat',`` to INSTALLED_APPS and the urls:

.. highlight:: python

::

   url('^chat/', include('rechat.urls')),

Settings
--------

.. highlight:: python

::

   # 1. Required
   
   SITE_SLUG = "mysite"
   
   # 2. Optional general settings:
   
   # rechat database: default is SITE_SLUG
   RECHAT_DB = "rechat"
   # rechat table: default is "chat"
   RECHAT_TABLE = "mychattable"
   
   # 3. Persistence
   
   # default: True
   USE_CACHE = False
   # default: 30
   RECHAT_CACHE_ITEMS = 20
   # default: 60*60*12 (12 hours)
   CHAT_CACHE_TTL = 60*60
   # default: localhost
   RECHAT_REDIS_HOST = 'ip_here'
   # default: 6379
   RECHAT_REDIS_PORT = 4867
   # default: 0
   RECHAT_REDIS_DB = 1
   
   # 4. History
   USE_HISTORY = True
   
You will need Redis to be installed to use persistence.  

If you use history create the database and table in Rethinkdb, and add a secondary index 
set to ``timestamp`` to the table. 

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
  
Templates
---------

Create a ``templates/instant/extra_clients.js`` with this content:

.. highlight:: python

::

   {% include "rechat/js/client.js" %}


  
  