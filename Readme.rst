Flask-Diamond
=============

Flask-Diamond is a batteries-included Flask framework. Easily scaffold a working application with sensible defaults, then override the defaults to customize it for your goals.

Overview
--------

Flask-Diamond imports many other Flask extensions and glues them all together.  The end result is a model administration view, accounts and high-level account operations (e.g. password reset), testing, documentation, deployment, and more.

Installation
^^^^^^^^^^^^

::

    mkvirtualenv Flask-Diamond
    pip install Flask-Diamond

Usage
^^^^^

::

    workon Flask-Diamond
    diamond-scaffold.sh ~/Documents/new-project
    cd ~/Documents/new-project
    mkvirtualenv -a . new-project
    make install docs test db server

Documentation
^^^^^^^^^^^^^

http://flask-diamond.readthedocs.org
