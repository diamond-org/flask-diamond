Flask-Diamond
=============

**Flask-Diamond** provides some opinions about data-centric Internet applications and systems.
**Flask-Diamond** is a batteries-included Flask framework, sortof like Django but radically decomposable.
Using **Flask-Diamond**, you can scaffold a working application with sensible defaults, then easily override those defaults to customize it for your own goals.
**Flask-Diamond** provides a shared vocabulary that helps teams coordinate as they scale up to develop multiple Flask applications while maintaining good code reuse and learning transfer.
**Flask-Diamond** goes beyond a "project scaffold" by providing a complete architecture and team solution, including documentation, tutorials, and other learning support.

Overview
--------

A Flask-Diamond application consists of *facets*, which are common facilities that many applications eventually need to provide.
The *facets* provided by Flask-Diamond include:

- account management
- administrative access
- databases
- Model object CRUD
- email
- testing
- documentation
- deployment
- and more

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

http://flask-diamond.org

Video Tutorial
^^^^^^^^^^^^^^

.. image:: https://img.youtube.com/vi/XqfF_du06uo/0.jpg
    :alt: Flask-Diamond Quick Start
    :target: https://www.youtube.com/watch?v=XqfF_du06uo
    :align: center
    :height: 315px
    :width: 560px
