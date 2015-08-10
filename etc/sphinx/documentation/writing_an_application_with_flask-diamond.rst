Writing an Application with Flask-Diamond
=========================================

This document is a work in progress.

A Simple Flask-Diamond Example
------------------------------

::

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

Create an object that inherits Flask-Diamond, then overload.

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

