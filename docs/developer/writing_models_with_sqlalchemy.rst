Models with SQLAlchemy
======================

In Flask-Diamond, a Model is a way of reading and writing a database. If our application is a chess game, then we're modeling chess objects in a database.  If our application is a social network, then we're modeling people objects in a database. A fundamental assumption of the :doc:`Model-View-Controller <model_view_controller_with_flask-diamond>` architecture is that our application deals with objects, and our objects are modeled after the things our application deals with.

This document will demonstrate a model, then discuss some of the ways Flask-Diamond makes it easier to work with models.

A Basic Model
-------------

A model is actually written in Flask-Diamond using Python.  Models are represented using `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_, which is a very powerful Python library for working with databases.  Since we are storing our models in a database, `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ provides a strong foundation for getting the job done.

Let's create a model of a person who has a name and an age.  Also, let's model the fact that every person has two biological parents (here called a mother and a father).  The following example demonstrates one way this model might be accomplished. [#f1]_

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

Model Methods
-------------

Usually, data models are created for entities that are changing.  A person's age increases every year, so we might create a *birthday* method that increments a person's age.  A simplified version of our person model has been extended with the birthday method below:

.. code-block:: python

    class Person(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))
        age = db.Column(db.Integer)

        def birthday(self):
            self.age += 1
            self.save()

Only The Model Controls the Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is important to contain any data-altering methods within your Model, or else there may be confusion down the road.  For example, if there is code within the Controller that directly alters the data Model, you should move that code from the Controller to a new Model method that achieves the same task.  Finally, in the controller, invoke the Model method.

SQLAlchemy
----------

`SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ and `Flask-SQLAlchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_ are used to provide an Object Relation Mapper (ORM), which reads/writes a database and makes the data easy to access using Python.  By using an ORM such as `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_, it is possible to avoid many pitfalls of directly using SQL, such as SQL injections or schema mismatches.  One of the best resources to learn about writing models is the `SQLAlchemy <http://docs.sqlalchemy.org/en/rel_1_0/>`_ documentation itself, which is both excellent and extensive.

Model Relationships with SQLAlchemy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `SQLAlchemy Basic Relationships <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html>`_ document provides an excellent overview of different relationship patterns, including:

- `One to Many <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-many>`_
- `Many to One <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-one>`_
- `One to One <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one>`_
- `Many to Many <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many>`_
- `Many to Many Association <http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#association-object>`_

To demonstrate a basic relationship, let's say each Person lives in a House, which is modeled as:

.. code-block:: python

    class House(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        address = db.Column(db.String(255))

    class Person(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        house_id = db.Column(db.Integer, db.ForeignKey("house.id"))
        house = db.relationship('House',
            backref=db.backref('persons', lazy='dynamic')
        )

The following code example uses the classes above to create two people who live at one house.

.. code-block:: python

    our_house = House(address="1600 Pennsylvania Ave")
    myself = Person("Me", house=our_house)
    mom = Person("Mom", house=our_house)
    print(myself.house)

Querying with SQLAlchemy
^^^^^^^^^^^^^^^^^^^^^^^^

Based on the Person class, a simple query that finds a person named "Me" looks like:

.. code-block:: python

    myself = models.Person.find(name="Me")
    print(myself.name)

However, the `SQLAlchemy Query API <http://docs.sqlalchemy.org/en/latest/orm/query.html>`_ is extremely powerful, and its documentation is the authoritative source.

When the Model Changes
----------------------

There is a close correspondence between the Model and the database tables.  If an attribute is added to a model, then we need a new column in our database to store the values for this attribute.  If the model changes, the database must also change.  There are two ways of updating your database:

- **the clean slate**: delete the old database and creating a new one that reflects the latest changes to the model.  This is accomplished with ``make db`` on the command line.  It's easy and quick.
- **schema migrations**: analyze your updated model to determine what parts are different from your old database, and then add/remove those parts to a live database.  This is tricky, but it is necessary for databases in production.  Read more in :doc:`managing_schemas_with_flask-migrate`.

As long as you are actively developing, it is recommended to use ``make db`` each time you update your model.  However, when your application is live, you will need to read :doc:`managing_schemas_with_flask-migrate` to learn about altering a production database.

Data Fixtures
-------------

What good is a data model without any data to put in it?  Data fixtures are a way of easily adding data to your database, which is helpful when you are frequently rebuilding your database with ``make db``.  Data fixtures can be placed into ``bin/manage.py`` within the ``populate_db()`` function.  If you find yourself continually re-creating certain model objects in your database so you can test your application, then consider using ``populate_db()`` to automate the creation of these objects.

For example, in order for ``make db`` to automatically create a Person object based on the Person class above, construct ``populate_db()`` like this:

.. code-block:: python

    @manager.command
    def populate_db():
        "insert a default set of objects"

        from models import Person

        me = Person.create(name="Me", age=34)
        mom = Person.create(name="Mom", age=65)
        dad = Person.create(name="Dad", age=64)
        me.mother = mom
        me.father = dad
        me.save()


Another model example
---------------------

.. code-block:: python

    class Individual(db.Model, CRUDMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))

        friend_id = db.Column(db.Integer, db.ForeignKey('individual.id'))
        friend = db.relationship('Individual',
            primaryjoin=('Individual.friend_id == Individual.id'),
            remote_side="Individual.id")

        def set_friend(self, obj):
            self.friend = obj
            self.save()

        def as_hash(self):
            pass

        def __str__(self):
            return self.name

Further Reading
---------------

- See :doc:`managing_schemas_with_flask-migrate`, which describes how to evolve the application database along with its Model.
- See :doc:`crud_with_flask-diamond`, which describes the Create-Read-Update-Delete pattern for Models.
- See :doc:`writing_a_gui_with_flask-admin`, which explains how to create a GUI for interacting with Models.

.. rubric:: Footnotes

.. [#f1] Note the use of CRUDMixin, which provides us with a create() method.  For more information about CRUDMixin, see :doc:`crud_with_flask-diamond`.