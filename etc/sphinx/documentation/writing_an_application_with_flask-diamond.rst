Writing an Application with Flask-Diamond
=========================================



This document is a work in progress.

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
------------------------------

In the basic example above, notice the two functions ``administration()`` and ``blueprints()``.  By overloading these two functions, as well as others in Flask-Diamond, it is possible to customize different aspects of your application.

Extending the Scaffold
----------------------

The files are a starting point.

Key Design Documents
--------------------

When it is time to actually work on your application, it can save time to sketch designs before implementing code.  

Entity Relationship Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wireframes
^^^^^^^^^^

Sitemap
^^^^^^^

