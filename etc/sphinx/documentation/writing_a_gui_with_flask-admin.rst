Writing a GUI with Flask-Admin
==============================

A common pattern in application design is to apply :doc:`CRUD <crud_with_flask-diamond>` to your :doc:`Model <writing_models_with_sqlalchemy>`, and then provide a Graphical User Interface for people to interact with the Model.  `Flask-Admin <http://flask-admin.readthedocs.org/>`_ makes it very easy to create a basic interface with Create-Read-Update-Delete functionality, and provides a framework for designing much more sophisticated interfaces.

This document discusses a simple CRUD with Flask-Admin, and then extends the CRUD with additional functionality.  When Flask-Admin creates a GUI, it automatically discovers the Model Attributes and creates a web form containing fields for all the attributes.  

A Simple CRUD GUI
-----------------

Flask-Admin provides the `BaseModelView <http://flask-admin.readthedocs.org/en/latest/api/mod_model/#flask_admin.model.BaseModelView>`_ class as the foundation for building Views that a user can interact with to inspect and control a Model.  Flask-Diamond provides `AdminModelView <http://flask-diamond.readthedocs.org/en/latest/api/#flask_diamond.administration.AdminModelView>`_, which applies an authentication requirement so that only users with the Admin role can access the View.

AdminModelViewExample
^^^^^^^^^^^^^^^^^^^^^

The following example imports a class called Person (which is described in the :doc:`Model documentation <writing_models_with_sqlalchemy>`).  Then, the Person class is added to the GUI using the `add_view() <http://flask-admin.readthedocs.org/en/latest/api/mod_base/#flask_admin.base.Admin.add_view>`_ method.

.. code-block:: python

    from flask.ext.diamond import Diamond, db, security
    from flask.ext.diamond.administration import AdminModelView
    from . import models

    class my_diamond_app(Diamond):
        def administration(self):
            admin = super(my_diamond_app, self).administration()
            admin.add_view(AdminModelView(
                models.Person,
                db.session,
                name="Person",
                category="Models")
            )

When the server is launched, it will now provide a GUI facility for applying CRUD operations to the Person model.  Due to the use of AdminModelView, the application will now require a password before allowing anybody to create, read, update, or delete any Person object.

The *category* parameter causes the GUI to put this View into the menu bar beneath the heading "Models".  The *name* parameter indicates this link will be titled *Person*.  Now you can find the Person CRUD by navigating through the menu to Models and then to Person.

Multiple CRUD Views Inside BaseModelView
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BaseModelView actually creates multiple views that provide CRUD functionality:

- **Create**: this view presents a form with all of the model attributes displayed as blank fields.  When the fields are populated and the form is submitted, a new model object will be created.
- **List**: the List view displays a paginated list of all the objects of the Model.  This view also contains widgets for editing and deleting objects.
- **Edit**: the Edit view is identical to the create view, except now the fields are populated by a specific model object.  When the fields are changed, the model object can be updated.
- **Delete**: The Delete view simply confirms whether the user wants to delete an object.

Create-List-Edit-Delete actually corresponds 

Extending the CRUD
------------------

In the :doc:`Model documentation <writing_models_with_sqlalchemy>`, the Person Model was extended with a birthday() method that causes the person to become one year older.  Flask-Admin makes it pretty easy to add custom functionality through `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ [#f1]_.

Adding a Widget
^^^^^^^^^^^^^^^

Exposing Another View
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Footnotes

.. [#f1] Incidentally, `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ is the same mechanism used by Flask-Diamond for customization.  Inheritance is discussed further in `writing_an_application_with_flask-diamond`.
