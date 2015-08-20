Writing an Application with Flask-Diamond
=========================================

By default, Flask-Diamond is ready to run when you initially scaffold a new application.  This document describes the customization process, which transforms the default application into something tailored to your goals.  We will start by discussing the default start-up routine for all Flask-Diamond applications, and then talk about modifying start-up to change its behavior.

A basic Flask-Diamond Example
-----------------------------

The following example can be generated from a freshly scaffolded project by following the :doc:`../documentation/project_initialization_and_scaffolding` document with the project name ``MyDiamondApp``.  Notice that the ``MyDiamondApp`` class inherits from ``Diamond``, which gives the new project a lot of functionality "out of the box."

.. code-block:: python

    from flask.ext.diamond import Diamond, db, security
    from flask.ext.diamond.administration import AdminModelView
    from . import models

    class MyDiamondApp(Diamond):
        def administration(self):
            admin = super(MyDiamondApp, self).administration()
            admin.add_view(AdminModelView(
                models.Individual,
                db.session,
                name="Individual",
                category="Models")
            return admin

        def blueprints(self):
            from flask_diamond.views.diamond import diamond_blueprint
            from .views.administration.modelviews import adminbaseview

            self.app.register_blueprint(diamond_blueprint)
            self.app.register_blueprint(adminbaseview)
            self.app.register_blueprint(baseview, url_prefix="/home")


    def create_app():
        app_instance = MyDiamondApp()
        app_instance.init_app()
        return app_instance.app

Customization with Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the basic example above, notice the two functions ``administration()`` and ``blueprints()``.  These functions handle the initialization of administration and blueprints, respectively.  By overloading [#f1]_ these functions (and others) within your application, it is possible to customize the start-up behavior of these subsystems.  Any subsystem in the Flask-Diamond start-up can be configured.  For a complete list of the functions you can overload, refer to the :ref:`diamond-object` documentation.

Disabling Functionality
^^^^^^^^^^^^^^^^^^^^^^^

Inheritance also permits functionality to be disabled.  For example, to completely disable email, it is possible to overload the email startup with a function that does nothing.  It looks like this:

.. code-block:: python

    def email(self):
        pass # do nothing

Many subsystems can be enabled/disabled with ease.  Other subsystems, like blueprints, are fundamental to the behavior of a Flask application, and are therefore trickier to disable in Flask-Diamond.

Application start-up
--------------------

Flask-Diamond initializes many subsystems when the application is first started.  The subsystems are initialized in this order:

#. **flask configuration**: the ``$SETTINGS`` environment variable is inspected and the file it points to is loaded.
#. **logging**: based on the configuration, write log messages to a file on the filesystem.
#. **sqlalchemy database**: connect to a database and initialize the SQLAlchemy Object Relational Mapper (ORM)
#. **flask blueprints**: initialize your application's views (in the MVC sense), which are saved as "blueprints" in a Flask application.
#. **forms**: initialize your application's web forms, which reads input from users and validates it.
#. **webassets**: it is possible to bundle assets like images, CSS, and javascript with your application.  webassets simplifies some of this work.
#. **debug toolbar**: when the configuration specifies that ``DEBUG = True``, the web interface will display a widget with extra debugging tools.
#. **flask signals**: Flask provides a signals subsystem that your application can hook into to automate certain behaviors.
#. **flask error handlers**: when something goes wrong, you may want to handle it (e.g. by displaying a 404 page)
#. **security**: manage users, roles, login, passwords, and other security things with Flask-Security.
#. **administration**: a quick GUI using Flask-Admin with extensive Model support.
#. **rest**: provide a REST API using Flask-RESTful
#. **email**: send email with Flask-Mail
#. **request handlers**: control the way Flask handles certain requests
#. **celery**: provide a task queue using Celery

The default behavior of these functions is described in the :ref:`diamond-object` documentation.

Extending the Scaffold
----------------------

The scaffold files are a starting point, and you will probably end up creating many new files in the course of writing your application.  You can think about the scaffold as being sortof similar to inheritance; if you want to change one of the default files, just overwrite it with your own.  By customizing the scaffold, you can easily create new models, views, security views, administration views, API endpoints, and more.

It is recommended to stick with the directory structure in the beginning.  As with anything, you are free to change the structure, but if you learn how to work within it, your applications will be easier to maintain and deploy - especially when you have dozens of Flask-Diamond applications to manage!

Further Reading
---------------

Several guides have been created to discuss Flask-Diamond application building in greater detail:

- :doc:`writing_models_with_sqlalchemy`
.. - :doc:`writing_a_gui_with_flask-admin`

.. rubric:: Footnotes

.. [#f1] "Overloading" is the process of creating a function with the same name as a function in the class you're inheriting from.  In the example above, we have overloaded ``administration()`` and ``blueprints()``.