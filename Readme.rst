Flask-Diamond
=============

**Flask-Diamond** is a batteries-included Python Flask framework, sortof like Django but radically decomposable.
**Flask-Diamond** offers some opinions about network information systems that process data.
Using **Flask-Diamond**, you can scaffold a working application with sensible defaults, then easily override those defaults to meet your own goals.
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

Usage on Windows
^^^^^^^^^^^^^^^^

The following steps will create a new Flask-Diamond application on a Windows machine.

::

    easy_install -U mr.bob==0.1.2
    pip install Flask-Diamond
    md my-application
    cd my-application
    flask-diamond scaffold app
    make install db-win server-win

Documentation
^^^^^^^^^^^^^

http://flask-diamond.org

Quick Start Screencast
^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://img.youtube.com/vi/dFp-YtV4898/0.jpg
    :alt: Flask-Diamond Quick Start
    :target: https://www.youtube.com/watch?v=dFp-YtV4898
    :align: center
    :height: 315px
    :width: 560px

Length: 3:17
