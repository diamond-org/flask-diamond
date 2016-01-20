Writing a GUI with Flask-Admin
==============================

A common pattern in application design is to apply :doc:`CRUD <crud_with_flask-diamond>` to your :doc:`Model <writing_models_with_sqlalchemy>`, and then provide a Graphical User Interface for people to interact with the Model.  `Flask-Admin <http://flask-admin.readthedocs.org/>`_ makes it very easy to create a basic interface with Create-Read-Update-Delete functionality, and provides a framework for designing much more sophisticated interfaces.

This document discusses a simple CRUD with `Flask-Admin <http://flask-admin.readthedocs.org/>`_, and then extends the CRUD with additional functionality.

A Simple CRUD GUI
-----------------

When `Flask-Admin <http://flask-admin.readthedocs.org/>`_ creates a GUI, it automatically discovers the Model Attributes and creates a web form containing fields for all the attributes.  Flask-Admin provides the `BaseModelView <http://flask-admin.readthedocs.org/en/latest/api/mod_model/#flask_admin.model.BaseModelView>`_ class as the foundation for building Views that a user can interact with to inspect and control a Model.  Flask-Diamond provides `AdminModelView <http://flask-diamond.readthedocs.org/en/latest/api/#flask_diamond.administration.AdminModelView>`_, which applies an authentication requirement so that only users with the Admin role can access the View.

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

When the server is launched, it provides a GUI facility for applying CRUD operations to the Person model.  Due to the use of AdminModelView, the application will now require a password before allowing anybody to create, read, update, or delete any Person object.

The *category* parameter causes the GUI to put this View into the menu bar beneath the heading "Models".  The *name* parameter indicates this link will be titled *Person*.  Now you can find the Person CRUD by navigating through the menu to Models and then to Person.

Multiple CRUD Views Inside BaseModelView
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BaseModelView actually creates multiple views that provide CRUD functionality:

- **Create**: this view presents a form with all of the model attributes displayed as blank fields.  When the fields are populated and the form is submitted, a new model object will be created.
- **List**: the List view displays a paginated list of all the objects of the Model.  This view also contains widgets for editing and deleting objects.
- **Edit**: the Edit view is identical to the create view, except now the fields are populated by a specific model object.  When the fields are changed, the model object can be updated.
- **Delete**: The Delete view simply confirms whether the user wants to delete an object.

Create-List-Edit-Delete corresponds directly to Create-Read-Update-Delete.

Extending the CRUD
------------------

Flask-Admin makes it pretty easy to add custom functionality through `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ [#f1]_.  In the :doc:`Model documentation <writing_models_with_sqlalchemy>`, the Person Model provides a birthday() method that causes the person to become one year older.  The following sections demonstrate how to expose the birthday method and create a user interface widget for calling that method.

Exposing a new View
^^^^^^^^^^^^^^^^^^^

In addition to the basic CRUD views, new views can be created for doing other things with Models.  Since the Person class has been extended with a birthday() method, the following example enables the method to be called through the Controller.

.. code-block:: python

    from flask.ext.admin import expose

    class PersonModelView(AdminModelView):
        @expose('/birthday/<person_id>')
        def birthday(self, person_id):
            the_person = models.Person.get(person_id)
            the_person.birthday()
            return flask.redirect(flask.url_for('.list_view'))

    class my_diamond_app(Diamond):
        def administration(self):
            admin = super(my_diamond_app, self).administration()
            admin.add_view(PersonModelView(
                models.Person,
                db.session,
                name="Person",
                category="Models")
            )


Adding a Widget
^^^^^^^^^^^^^^^

One simple way to add functionality to the user interface is to use Flask-Admin's formatters to make a field into an interactive widget.  This basic pattern is demonstrated by formatting Person.age with a "birthday" button:

.. code-block:: python

    import jinja2

    class PersonModelView(AdminModelView):
        def age_formatter(self, context, model, name):
            age_widget_template = "{0} <a href='{1}'>birthday!</a>"
            age_widget = age_widget_template.format(
                model.age,
                flask.url_for(".birthday", person_id=model.id)
            )
            return jinja2.Markup(age_widget)

        column_formatters = {
            "age": age_formatter,
        }

When these two *PersonModelView* examples are combined, the result is a user interface that can model a Person's birthday when a link is clicked.

ModelView Example
^^^^^^^^^^^^^^^^^

The following ``AuthModelView`` includes examples for overriding various fields within the model view.  The full documentation for ModelView should be consulted for more information, but this example is intended to describe how that information may be applied within a Flask-Diamond project.

.. code-block:: python

    class IndividualAdmin(AuthModelView):

        edit_template = 'individual_view.html'

        column_list = ("name", "friend")

        form_overrides = {
            "upload_buffer": FileUploadField
        }

        form_args = {
            'upload_buffer': {
                'label': 'Report PDF',
                'base_path': "/tmp",
            }
        }

More Flask-Admin
^^^^^^^^^^^^^^^^

Flask-Admin is really powerful, and the best way to learn more is by `reading the Flask-Admin documentation <http://flask-admin.readthedocs.org/en/latest/introduction/>`_.

Further Reading
---------------

- See :doc:`crud_with_flask-diamond`, which describes the Create-Read-Update-Delete pattern for Models.
- See :doc:`writing_models_with_sqlalchemy` for a more detailed examination of Models.

.. rubric:: Footnotes

.. [#f1] Incidentally, `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ is the same mechanism used by Flask-Diamond for customization.  Inheritance is discussed further in `writing_an_application_with_flask-diamond`.
