CRUD with Flask-Diamond
=======================

Create Read Update Delete
-------------------------

CRUD stands for Create, Read, Update, and Delete. The CRUD pattern complements :doc:`Model-View-Controller <model_view_controller_with_flask-diamond>` by providing a standard set of methods that can be applied to most types of models.  CRUD acts like a simple API for models in Flask-Diamond. The four CRUD actions describe the life-cycle of a model object:

#. First, an object is **created** with certain attribute values.
#. The object may be **read** to get the value of those object attributes.
#. The object values may be **updated** to update the model based on changes in the world.
#. Finally, the object is **deleted** to remove it from the database.

CRUDMixin
---------

:class:`flask_diamond.mixins.crud.CRUDMixin`, which has been adapted from `Flask-Kit <https://github.com/semirook/flask-kit/blob/master/base/models.py>`_, will extend your model with functions for ``create()``, ``read()``, ``update()``, and ``delete()``.  The default Flask-Diamond scaffold provides an example of CRUDMixin usage:

.. code-block:: python

    from flask.ext.diamond.utils.mixins import CRUDMixin
    from flask.ext.diamond import db

    class Person(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))
        age = db.Column(db.Integer)

Notice that ``class Person()`` inherits both ``db.Model`` and ``CRUDMixin``.  Now the following CRUD workflow is possible:

.. code-block:: python

    myself = Person.create(name="me", age=34) # create
    print "{name} is {age} years old".format(myself)
    myself.update({'age': 35}) # update
    print "{name} is now {age} years old".format(myself)
    myself.delete()

Flask-Admin CRUD
----------------

`Flask-Admin <http://flask-admin.readthedocs.org/>`_ provides Model CRUD functionality with its `BaseModelView <http://flask-admin.readthedocs.org/en/latest/api/mod_model/#flask_admin.model.BaseModelView>`_ class.  ``BaseModelView`` is an extremely powerful tool for rapidly implementing a web-based CRUD Graphical User Interface that makes it easy to create, read, update, and delete model objects using a web browser.

The following application instantiates a CRUD for the ``Person`` model described above.

.. code-block:: python

    from flask.ext.diamond import Diamond, db
    from flask.ext.diamond.administration import AdminModelView
    from . import models

    class my_diamond_app(Diamond):
        def administration(self):
            admin = super(my_diamond_app, self).administration()
            admin.add_view(AdminModelView(
                models.Person,
                db.session,
                name="Person",
                category="Admin"
                )
            )

Further Reading
---------------

- See :doc:`writing_models_with_sqlalchemy` for a more detailed examination of Models.
- See :doc:`writing_a_gui_with_flask-admin` for a more detailed examination of GUIs.
