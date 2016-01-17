# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database(self):
    """
    Initialize database

    :returns: None

    Flask-Diamond assumes you are modelling your solution using an Entity-
    Relationship framework, and that the application will use a relational
    database (e.g. MySQL, Postgres, or SQlite3) for model persistence.
    Thus, `SQLAlchemy
    <http://docs.sqlalchemy.org/en/rel_0_9/contents.html>`_ and `Flask-
    SQLalchemy <https://pythonhosted.org/Flask-SQLAlchemy/index.html>`_
    are used for database operations.

    Typically, this just works as long as ``SQLALCHEMY_DATABASE_URI`` is
    set correctly in the application configuration.
    """

    db.app = self.app
    db.init_app(self.app)
