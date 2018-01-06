Install
=======

Websockets server
-----------------

Install `Django Instant <https://github.com/synw/django-instant>`_ .

Instructions are `here <http://django-instant.readthedocs.io/en/latest/src/install.html>`_

``pip install redis django-mqueue``

Add to INSTALLED_APPS;

.. highlight:: python

::
   
   'rechat',
   'mqueue',
   

Set the urls:
  
.. highlight:: python

::

   from instant.views import instant_auth
   
   urlpatterns = [
   	# ...
   	url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
   	url('^chat/', include('rechat.urls')),
   	]
   	
Run the migrations

Settings
--------

.. highlight:: python

::

   # Required
   
   SITE_SLUG = "mysite"
   INSTANT_USERS_CHANNELS = [
    ["$" + SITE_SLUG + "_chat", ["/chat"]]
   ]
   
   # Optional
   
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

   
You will need Redis to be installed to use the cache.  

Only the logged in users can chat.

Templates
---------

Create a ``templates/instant/handlers/$mysite_chat`` (where mysite is the value of the
``SITE_SLUG`` setting). Fill it with this content:

.. highlight:: python

::

   {% include "rechat/js/handler.js" %}
   


  
  