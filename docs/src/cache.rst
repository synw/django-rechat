Cache management
================

By default the cache is enabled. You have to install and run Redis.

Optional: in settings.py:

.. highlight:: python

::

   # Redis host: default is localhost
   RECHAT_REDIS_HOST = 'ip_here'
   # Redis port: default is 6379
   RECHAT_REDIS_PORT = 5555
   # Redis db: default is 0
   RECHAT_REDIS_DB = 1
   
   # number of cached items: default is 30
   RECHAT_CACHE = 20
   # cache time to live in seconds: default is 60*60*12
   RECHAT_CACHE_TTL = 60*60
   
The cache is used to load the last messages when a user reloads a page. The cache can be disabled so that the 
messages are only broadcasted to the socket, not stored. To disable the cache in settings.py:

.. highlight:: python

::

   RECHAT_USE_CACHE = False