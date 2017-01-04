Facet: Administration
=====================

A common pattern in application design is to apply :doc:`CRUD <crud>` to your :doc:`Model <models>`, and then provide a Graphical User Interface for people to interact with the Model.  `Flask-Admin <http://flask-admin.readthedocs.org/>`_ makes it very easy to create a basic interface with Create-Read-Update-Delete functionality, and provides a framework for designing much more sophisticated interfaces.

This document discusses a simple CRUD with `Flask-Admin <http://flask-admin.readthedocs.org/>`_, and then extends the CRUD with additional functionality.

A Simple CRUD GUI
-----------------

When `Flask-Admin <http://flask-admin.readthedocs.org/>`_ creates a GUI, it automatically discovers the Model Attributes and creates a web form containing fields for all the attributes.  Flask-Admin provides the `BaseModelView <http://flask-admin.readthedocs.org/en/latest/api/mod_model/#flask_admin.model.BaseModelView>`_ class as the foundation for building Views that a user can interact with to inspect and control a Model.  Flask-Diamond provides `AdminModelView <http://flask-diamond.readthedocs.org/en/latest/api/#flask_diamond.administration.AdminModelView>`_, which applies an authentication requirement so that only users with the Admin role can access the View.

AdminModelViewExample
^^^^^^^^^^^^^^^^^^^^^

The following example imports a class called Planet (which is described in the :doc:`Model documentation <models>`).  Then, the Planet class is added to the GUI using the `add_view() <http://flask-admin.readthedocs.org/en/latest/api/mod_base/#flask_admin.base.Admin.add_view>`_ method.

.. code-block:: python

    from flask_diamond import Diamond
    from flask_diamond.administration import AdminModelView
    from .models import User, Role, Planet

    class my_diamond_app(Diamond):

        def init_administration(self):
            admin = self.super("administration", user=User, role=Role)
            admin.add_view(AdminModelView(
                Planet,
                db.session,
                name="Planet",
                category="Admin")
            )

When the server is launched, it provides a GUI facility for applying CRUD operations to the Planet model.  Due to the use of AdminModelView, the application will now require a password before allowing anybody to create, read, update, or delete any Planet object.

The *category* parameter causes the GUI to put this View into the menu bar beneath the heading "ModelAdmin".  The *name* parameter indicates this link will be titled *Planet*.  Now you can find the Planet CRUD by navigating through the menu to Models and then to Planet.

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

Flask-Admin makes it pretty easy to add custom functionality through `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ [#f1]_.
In the :doc:`Model documentation <models>`, the Planet Model provides a ``bombard()`` method that sends an asteroid at a planet.
The following sections demonstrate how to expose the ``bombard()`` method and create a user interface widget for calling that method.

Exposing a new View
^^^^^^^^^^^^^^^^^^^

In addition to the basic CRUD views, new views can be created for doing other things with Models.
Since the Planet class has been extended with a bombard() method, let's create a URL endpoint to send an asteroid at a planet.

.. code-block:: python

    from flask_diamond import Diamond
    from flask_diamond.administration import AdminModelView
    from flask_admin import expose
    from .models import User, Role, Planet

    class PlanetModelView(AdminModelView):
        @expose('/bombard/<planet_id>')
        def bombard(self, planet_id):
            the_planet = models.Planet.get(planet_id)
            the_planet.bombard(mass=10.0)
            return flask.redirect(flask.url_for('.list_view'))

    class my_diamond_app(Diamond):
        def init_administration(self):
            admin = self.super("administration", user=User, role=Role)
            admin.add_view(PlanetModelView(
                models.Planet,
                db.session,
                name="Planet",
                category="Admin")
            )


Adding a Widget
^^^^^^^^^^^^^^^

One simple way to add functionality to the user interface is to use Flask-Admin's formatters to make a field into an interactive widget.  This basic pattern is demonstrated by formatting Planet.mass with a "bombard" button:

.. code-block:: python

    import jinja2
    from flask_diamond import Diamond
    from flask_diamond.administration import AdminModelView
    from flask_admin import expose
    from .models import User, Role, Planet

    class PlanetModelView(AdminModelView):
        def mass_formatter(self, context, model, name):
            mass_widget_template = "{0} <a href='{1}'>bombard!</a>"
            mass_widget = mass_widget_template.format(
                model.age,
                flask.url_for(".bombard", planet_id=model.id)
            )
            return jinja2.Markup(mass_widget)

        column_formatters = {
            "age": mass_formatter,
        }

When these two *PlanetModelView* examples are combined, the result is a user interface that can bombard a planet with asteroids when clicked.

ModelView Example
^^^^^^^^^^^^^^^^^

The following ``AuthModelView`` includes examples for overriding various fields within the model view.  The full documentation for ModelView should be consulted for more information, but this example is intended to describe how that information may be applied within a Flask-Diamond project.

.. code-block:: python

    class PlanetAdmin(AuthModelView):

        edit_template = 'planet_edit.html'

        column_list = ("name", "mass")

        form_overrides = {
            "upload_buffer": FileUploadField
        }

        form_args = {
            'upload_buffer': {
                'label': 'Planet PDF',
                'base_path': "/tmp",
            }
        }

More Flask-Admin
^^^^^^^^^^^^^^^^

Flask-Admin is really powerful, and the best way to learn more is by `reading the Flask-Admin documentation <http://flask-admin.readthedocs.org/en/latest/introduction/>`_.

Further Reading
---------------

- See :doc:`crud`, which describes the Create-Read-Update-Delete pattern for Models.
- See :doc:`models` for a more detailed examination of Models.

.. rubric:: Footnotes

.. [#f1] Incidentally, `Python class inheritance <https://docs.python.org/2/tutorial/classes.html>`_ is the same mechanism used by Flask-Diamond for customization.  Inheritance is discussed further in `writing_an_application_with_flask-diamond`.
