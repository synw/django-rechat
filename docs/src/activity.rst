Activity widget
===============

To use the graphical activity monitoring widget add this content
in ``templates/instant/extra_clients.js``:

.. highlight:: django

::

   {% include "rechat/js/activity_client.js" %}
   
Be sure to load ``<script type="text/javascript" src="{% static 'rechat/js/smoothie.js' %}"></script>`` 
before including the client.

Then you can use it in your templates:

.. highlight:: django

::

   <canvas id="chart" width="600" height="100"></canvas>