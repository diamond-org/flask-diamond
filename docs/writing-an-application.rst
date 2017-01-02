Writing an Application with Flask-Diamond
=========================================

By default, Flask-Diamond is ready to run when you initially scaffold a new application.  This document describes the customization process, which transforms the default application into something tailored to your goals.  We will start by discussing the default start-up routine for all Flask-Diamond applications, and then talk about modifying start-up to change its behavior.

A basic Flask-Diamond Example
-----------------------------

The following example can be generated from a freshly scaffolded project by following the :doc:`scaffolding` document with the project name ``MyDiamondApp``.  Notice that the ``MyDiamondApp`` class inherits from ``Diamond``, which gives the new project a lot of functionality "out of the box."

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

Flask-Diamond applications initialize the following facets during startup:

#. :class:`flask_diamond.facets.configuration`
#. :class:`flask_diamond.facets.logs`
#. :class:`flask_diamond.facets.database`
#. :class:`flask_diamond.facets.accounts`
#. :class:`flask_diamond.facets.blueprints`
#. :class:`flask_diamond.facets.signals`
#. :class:`flask_diamond.facets.forms`
#. :class:`flask_diamond.facets.handlers`
#. :class:`flask_diamond.facets.administration`
#. :class:`flask_diamond.facets.rest`
#. :class:`flask_diamond.facets.webassets`
#. :class:`flask_diamond.facets.email`
#. :class:`flask_diamond.facets.debugger`
#. :class:`flask_diamond.facets.task_queue`

See :doc:`facets` for an overview of the specific facets that ship with Flask-Diamond.

Extending the Scaffold
----------------------

The scaffold files are a starting point, and you will probably end up creating many new files in the course of writing your application.  You can think about the scaffold as being sortof similar to inheritance; if you want to change one of the default files, just overwrite it with your own.  By customizing the scaffold, you can easily create new models, views, security views, administration views, API endpoints, and more.

Additional scaffolds are distributed along with Flask-Diamond.  They are stored in ``$VIRTUAL_ENV/share/skels`` and can be applied manually using ``mr.bob``.  Additional scaffolds describe common patterns for using Views and Models.

It is recommended to stick with the directory structure in the beginning.  As with anything, you are free to change the structure, but if you learn how to work within it, your applications will be easier to maintain and deploy - especially when you have dozens of Flask-Diamond applications to manage!

Further Reading
---------------

Several guides have been created to discuss Flask-Diamond application building in greater detail:

- :doc:`models`
- :doc:`administration`
- :doc:`blueprints`

.. rubric:: Footnotes

.. [#f1] "Overloading" is the process of creating a function with the same name as a function in the class you're inheriting from.  In the example above, we have overloaded ``administration()`` and ``blueprints()``.
