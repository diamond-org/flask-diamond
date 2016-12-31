Flask-Diamond
=============

Flask-Diamond is a batteries-included Flask framework. Easily scaffold a working application with sensible defaults, then override the defaults to customize it for your goals.

Overview
--------

Flask-Diamond imports many other Flask extensions and glues them all together.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, deployment, and more.

Usage
^^^^^

The following steps will create a new Flask-Diamond application.

::

    pip install Flask-Diamond
    mkdir my-application
    cd my-application
    flask-diamond scaffold app
    make install docs test db server

Please read the `Introduction Documentation <http://flask-diamond.readthedocs.io/en/latest/#get-started>`_ to get started.

Documentation
^^^^^^^^^^^^^

http://flask-diamond.readthedocs.org
