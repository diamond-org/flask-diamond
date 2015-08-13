Writing Models with SQLAlchemy
==============================

In Flask-Diamond, a Model is a way of reading and writing a database. If our application is a chess game, then we're modeling chess objects in a database.  If our application is a social network, then we're modeling people objects in a database. A fundamental assumption of the :doc:`Model-View-Controller <model_view_controller_with_flask-diamond>` architecture is that our application deals with objects, and our objects are modeled after the things our application deals with.

This document will demonstrate a model, then discuss some of the ways Flask-Diamond makes it easier to work with models.

A Basic Model
-------------

A model is actually written in Flask-Diamond using Python.  Models are represented using `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_, which is a very powerful Python library for working with databases.  Since we are storing our models in a database, `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ provides a strong foundation for getting the job done.

Let's create a model of a person who has a name and an age.  Also, let's model the fact that every person has two biological parents (here called a mother and a father).  The following example demonstrates one way this model might be accomplished.

.. code-block:: python

    from flask.ext.diamond.utils.mixins import CRUDMixin
    from .. import db


    class Person(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))
        age = db.Column(db.Integer)

        mother_id = db.Column(db.Integer, db.ForeignKey('person.id'))
        mother = db.relationship('Person',
            primaryjoin=('Person.mother_id == Person.id'),
            remote_side="Person.id")

        father_id = db.Column(db.Integer, db.ForeignKey('person.id'))
        father = db.relationship('Person',
            primaryjoin=('Person.father_id == Person.id'),
            remote_side="Person.id")

        def __str__(self):
            return self.name

Now, we can model a Person and specify their name and age.  Once we create Person objects for a mother and a father, we can model the parent-child relationships.  The model above could be used in Python like so:

.. code-block:: python

    from models import Person

    me = Person.create(name="Me", age=34)
    mom = Person.create(name="Mom", age=65)
    dad = Person.create(name="Dad", age=64)
    me.mother = mom
    me.father = dad
    me.save()

SQLAlchemy
----------

`SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ and `Flask-SQLAlchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_ are used to provide an Object Relation Mapper (ORM), which reads/writes a database and makes the data easy to access using Python.  By using an ORM such as `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_, it is possible to avoid many pitfalls of directly using SQL, such as SQL injections or schema mismatches.  One of the best resources to learn about writing models is the `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ documentation itself, which is both excellent and extensive.

When the Model Changes
----------------------

There is a close correspondence between the Model and the database tables.  If an attribute is added to a model, then we need a new column in our database to store the values for this attribute.  If the model changes, the database must also change.  There are two ways of updating your database:

- **the clean slate**: delete the old database and creating a new one that reflects the latest changes to the model.  This is accomplished with ``make db`` on the command line.  It's easy and quick.
- **schema migrations**: analyze your updated model to determine what parts are different from your old database, and then add/remove those parts to a live database.  This is tricky, but it is necessary for databases in production.  Read more in :doc:`schema_management_with_flask-migrations`.

As long as you are actively developing, it is recommended to use ``make db`` each time you update your model.  However, when your application is live, you will need to read :doc:`schema_management_with_flask-migrations` to learn about altering a production database.

Data Fixtures
-------------

What good is a data model without any data to put in it?  Data fixtures are a way of easily adding data to your database, which is helpful when you are frequently rebuilding your database with ``make db``.  Data fixtures can be placed into ``bin/manage.py`` within the ``populate_db()`` function.  If you find yourself continually re-creating certain model objects in your database so you can test your application, then consider using ``populate_db()`` to automate the creation of these objects.

A Philosophy of Models
----------------------

A model might be a very simple representation of a real thing, or the model might be very detailed.  For example, a model of an entire country's economy might require lots of detail, whereas a model of a school district might be relatively simpler.

Sometimes, we talk about "domains" when we talk about models, because our models might be thematically related to one another.  We might then say we're modeling a domain, and we might talk to a "domain expert" to learn more about the kinds of models we are building.

A model is in some ways a representationally platonic ideal compared to the actual domain being modeled.  While things in the "real world" are irregular in an uncountable number of ways, our models are perfectly regular.  Since models are stored in a database, all of the model attributes can be lined up nicely into rows and columns.

On the same coin, a model is always an imperfect representation of the thing it is modeling.  The irregularities of the real world are difficult to capture using a model.  The goal for good model creation is to isolate the parts of the model that are regular so as to reduce the number of exceptions to your model.

CRUDMixin and MarshmallowMixin
------------------------------

Flask-Diamond provides a few Python mixins for convenience:

- ``CRUDMixin`` will extend your model with functions for ``create()``, ``read()``, ``update()``, and ``delete()``.  These four key functions are widely used in a pattern called CRUD, which describes a basic lifecycle for model objects.  First an object is created, then it is alternately read and updated, and finally it is deleted.
- ``MarshmallowMixin`` simplifies object marshalling, which is the process of mapping data to and from a serialization format like JSON.  This is useful because applications must frequently send model data across the Internet, and in order to do so, models are commonly translated into JSON or another format.  Marshalling makes serialization and deserialization into a repeatable process.
