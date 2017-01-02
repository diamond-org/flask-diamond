Application Facets
==================

A Flask-Diamond application consists of many components (called *facets*) that complement each other to form a coherent application.  These facets are common to many applications, but they can be enabled and disabled individually depending on specific requirements.  A Flask-Diamond application is customized by changing the way these facets behave.

List of Facets
--------------

Here are all of the facets currently shipping with Flask-Diamond:

#. :class:`flask_diamond.facets.configuration`.  the ``$SETTINGS`` environment variable is inspected and the file it points to is loaded.
#. :class:`flask_diamond.facets.logs`.  based on the configuration, write log messages to a file on the filesystem.
#. :class:`flask_diamond.facets.database`.  connect to a database and initialize the SQLAlchemy Object Relational Mapper (ORM)
#. :class:`flask_diamond.facets.accounts`.  manage users, roles, login, passwords, and other security things with Flask-Security.
#. :class:`flask_diamond.facets.blueprints`.  initialize your application's views (in the MVC sense), which are saved as "blueprints" in a Flask application.
#. :class:`flask_diamond.facets.signals`.  Flask provides a signals subsystem that your application can hook into to automate certain behaviors.
#. :class:`flask_diamond.facets.forms`.  initialize your application's form helpers, which may be global to the forms used in your application.
#. :class:`flask_diamond.facets.handlers`.  when something goes wrong, you may want to handle it (e.g. by displaying a 404 page).  This is the place to create redirections or other custom request handlers that extend beyond views.
#. :class:`flask_diamond.facets.administration`.  a quick GUI using Flask-Admin with extensive Model support.
#. :class:`flask_diamond.facets.rest`.  provide a REST API using Flask-RESTful
#. :class:`flask_diamond.facets.webassets`.  it is possible to bundle assets like images, CSS, and javascript with your application.  webassets simplifies some of this work.
#. :class:`flask_diamond.facets.email`.  send email with Flask-Mail
#. :class:`flask_diamond.facets.debugger`.  when the configuration specifies that ``DEBUG = True``, the web interface will display a widget with extra debugging tools.
#. :class:`flask_diamond.facets.task_queue`.  provide a task queue using Celery

Next Steps
----------

Now that you know what facets are, learn how to use them by :doc:`writing-an-application`.
