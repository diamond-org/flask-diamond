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

    mkdir my-application
    cd my-application
    mkvirtualenv -a . my-application
    pip install Flask-Diamond
    flask-diamond app .
    make install docs test db server

Please read the `Introduction Documentation <http://flask-diamond.readthedocs.io/en/latest/#introduction>`_ to get started.

Documentation
^^^^^^^^^^^^^

http://flask-diamond.readthedocs.org
