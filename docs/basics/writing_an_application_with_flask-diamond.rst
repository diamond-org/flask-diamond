Writing an Application with Flask-Diamond
=========================================

By default, Flask-Diamond is ready to run when you initially scaffold a new application.  This document describes the customization process, which transforms the default application into something tailored to your goals.  We will start by discussing the default start-up routine for all Flask-Diamond applications, and then talk about modifying start-up to change its behavior.

A basic Flask-Diamond Example
-----------------------------

The following example can be generated from a freshly scaffolded project by following the :doc:`project_initialization_and_scaffolding` document with the project name ``MyDiamondApp``.  Notice that the ``MyDiamondApp`` class inherits from ``Diamond``, which gives the new project a lot of functionality "out of the box."

.. code-block:: python

    from flask.ext.diamond import Diamond, db
    from flask.ext.diamond.facets.administration import AdminView, AdminModelView
    app_instance = None
    from . import models

    class MyDiamondApp(Diamond):
        def init_blueprints(self):
            self.super("blueprints")
            from .views.administration.modelviews import adminbaseview
            self.app.register_blueprint(adminbaseview)

    def create_app():
        global application
        if not application:
            application = Diamond()
            application.facet("configuration")
            application.facet("logs")
            application.facet("database")
            application.facet("marshalling")
            application.facet("accounts")
            application.facet("blueprints")
            application.facet("signals")
            application.facet("forms")
            application.facet("error_handlers")
            application.facet("request_handlers")
            application.facet("administration")
            # application.facet("rest")
            # application.facet("webassets")
            # application.facet("email")
            # application.facet("debugger")
            # application.facet("task_queue")
        return application.app

Customization with Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the basic example above, notice the function ``blueprints()``.  This function handles the initialization of Flask blueprints.  By overloading [#f1]_ this functions (and others) within your application, it is possible to customize the start-up behavior of any subsystem.  Every subsystem in the Flask-Diamond start-up can be configured.  For a complete list of the functions you can overload, refer to the **extensions** argument in the :ref:`diamond-object` documentation.

Enable or Disable Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Flask-Diamond functionality is initialized using extensions.  In case you wish to disable certain functionality, you may simply omit that initialization step from the extensions list.  For example, to enable REST functionality, omit email initialization from the extensions passed to create_app().  Many extensions can be enabled/disabled with ease, including rest, webassets, email, debugger, and task_queue.

Other extensions, like blueprints, are fundamental to the behavior of a Flask application, and are therefore trickier to disable in Flask-Diamond.  In those cases, it may be better to override the initialization function using inheritance.

Inheritance also permits functionality to be disabled.  For example, to completely disable email, it is possible to overload the email startup with a function that does nothing.  It looks like this:

.. code-block:: python

    def init_email(self):
        pass # do nothing

Application start-up
--------------------

Flask-Diamond initializes many subsystems when the application is first started.  The subsystems are initialized in this order:

#. :class:`flask_diamond.facets.configuration`.  the ``$SETTINGS`` environment variable is inspected and the file it points to is loaded.
#. :class:`flask_diamond.facets.logs`.  based on the configuration, write log messages to a file on the filesystem.
#. :class:`flask_diamond.facets.database`.  connect to a database and initialize the SQLAlchemy Object Relational Mapper (ORM)
#. :class:`flask_diamond.facets.accounts`.  manage users, roles, login, passwords, and other security things with Flask-Security.
#. :class:`flask_diamond.facets.blueprints`.  initialize your application's views (in the MVC sense), which are saved as "blueprints" in a Flask application.
#. :class:`flask_diamond.facets.signals`.  Flask provides a signals subsystem that your application can hook into to automate certain behaviors.
#. :class:`flask_diamond.facets.forms`.  initialize your application's form helpers, which may be global to the forms used in your application.
#. :class:`flask_diamond.facets.handlers`.  when something goes wrong, you may want to handle it (e.g. by displaying a 404 page)
#. :class:`flask_diamond.facets.handlers`.  This is the place to create redirections or other custom request handlers that extend beyond views.
#. :class:`flask_diamond.facets.administration`.  a quick GUI using Flask-Admin with extensive Model support.
#. :class:`flask_diamond.facets.rest`.  provide a REST API using Flask-RESTful
#. :class:`flask_diamond.facets.webassets`.  it is possible to bundle assets like images, CSS, and javascript with your application.  webassets simplifies some of this work.
#. :class:`flask_diamond.facets.email`.  send email with Flask-Mail
#. :class:`flask_diamond.facets.debugger`.  when the configuration specifies that ``DEBUG = True``, the web interface will display a widget with extra debugging tools.
#. :class:`flask_diamond.facets.task_queue`.  provide a task queue using Celery

Extending the Scaffold
----------------------

The scaffold files are a starting point, and you will probably end up creating many new files in the course of writing your application.  You can think about the scaffold as being sortof similar to inheritance; if you want to change one of the default files, just overwrite it with your own.  By customizing the scaffold, you can easily create new models, views, security views, administration views, API endpoints, and more.

Additional scaffolds are distributed along with Flask-Diamond.  They are stored in ``$VIRTUAL_ENV/share/skels`` and can be applied manually using ``mr.bob``.  Additional scaffolds describe common patterns for using Views and Models.

It is recommended to stick with the directory structure in the beginning.  As with anything, you are free to change the structure, but if you learn how to work within it, your applications will be easier to maintain and deploy - especially when you have dozens of Flask-Diamond applications to manage!

Further Reading
---------------

Several guides have been created to discuss Flask-Diamond application building in greater detail:

- :doc:`/developer/writing_models_with_sqlalchemy`
- :doc:`/developer/writing_a_gui_with_flask-admin`
- :doc:`/developer/writing_views_with_jinja_and_blueprints`

.. rubric:: Footnotes

.. [#f1] "Overloading" is the process of creating a function with the same name as a function in the class you're inheriting from.  In the example above, we have overloaded ``administration()`` and ``blueprints()``.