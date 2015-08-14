CRUD with Flask-Diamond
=======================

Create-Read-Update-Delete
-------------------------

CRUD stands for Create, Read, Update, and Delete.  These four actions describe the life-cycle of a model object.  The CRUD pattern complements :doc:`Model-View-Controller <model_view_controller_with_flask-diamond>` by providing a standard set of methods that can be applied to most types of models.

Flask-Admin CRUD
----------------

Flask-Admin provides Model CRUD with its ModelView class.

CRUDMixin
---------

``CRUDMixin`` will extend your model with functions for ``create()``, ``read()``, ``update()``, and ``delete()``.  These four key functions are widely used in a pattern called CRUD, which describes a basic lifecycle for model objects.  First an object is created, then it is alternately read and updated, and finally it is deleted.

MarshmallowMixin
----------------

``MarshmallowMixin`` simplifies object marshalling, which is the process of mapping data to and from a serialization format like JSON.  This is useful because applications must frequently send model data across the Internet, and in order to do so, models are commonly translated into JSON or another format.  Marshalling makes serialization and deserialization into a repeatable process.
