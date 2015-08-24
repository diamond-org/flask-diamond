Writing Views with jinja and blueprints
=======================================

As is explained in :doc:`model_view_controller_with_flask-diamond`, a *View* takes data from a Model and presents it (typically to a user).  Often times, there are multiple Views of a data Model, and they may present different aspects of the Model.  A common pattern for multiple views is the use of permissions to restrict functionality to users based upon their account role.  The administrator may have a special *View* into the data that provides extra functionality that regular users do not have.

Views are frequently written using *templates*, which have placeholders for variables that may be filled in by the application.  In Flask-Diamond, the `Jinja templating language <http://jinja.pocoo.org/>`_ is used to generate HTML, javascript, CSS, and other web-facing files that create a user interface.  By populating the template with data from the Model, the result is that users can interact with Model data.

Jinja is a Templating Language
------------------------------

The `Jinja website <http://jinja.pocoo.org/>`_ provides a nice example of what Jinja looks like:

::

    {% extends "layout.html" %}
    {% block body %}
      <ul>
      {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
      {% endfor %}
      </ul>
    {% endblock %}

Variables in Jinja
^^^^^^^^^^^^^^^^^^

A python expression is denoted using double-curlies as ``{{ }}``.  In this manner, it is easy to reference variables 

Logic in Jinja
^^^^^^^^^^^^^^

Rendering a template with Flask
-------------------------------



Flask Blueprints: a Collection of Views
---------------------------------------

