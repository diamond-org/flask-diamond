Planets Tutorial
================

The Planets Tutorial will introduce Flask-Diamond by demonstrating a simple web application that manages Planets and Satellites in a database.
This tutorial assumes you have already installed the :doc:`system-requirements`.

Screencast
----------

.. raw:: html

    <center>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/XqfF_du06uo" frameborder="0" allowfullscreen></iframe>
    </center>

Overview
--------

The Planets Tutorial consists of two parts:

1. This document, which contains instructions and explanations
2. The Planets code scaffold, which can be installed from the command line

Simply follow the tutorial and we'll install everything, then use it to demonstrate some useful principles about Flask-Diamond applications.

Setup for Tutorial
------------------

The following commands will prepare you to begin the tutorial:

::

    mkdir planets
    cd planets
    mkvirtualenv -a . planets
    pip install Flask-Diamond
    flask-diamond scaffold app

For a more detailed explanation of these commands, please see the :doc:`quick-start`.
When you run ``flask-diamond scaffold app``, you will be prompted to answer some questions.
Give your application and module the name of ``planets`` during scaffolding.
For all other questions, you can accept the default answers by pressing Enter for each question.

Planets Application
-------------------

Now, we'll use a special scaffold called ``tutorial-planets`` for the rest of this tutorial.
The ``tutorial-planets`` scaffold places some example models and views into the application structure.

::

    flask-diamond scaffold tutorial-planets
    make test db server
    open http://localhost:5000

Your web browser should now display the ``planets`` application.
If you ran into problems, please review the :doc:`quick-start` to ensure you have all the requirements installed and working.

Make some Planets
-----------------

The 

- create earth
- update Planet model to print name instead of object
- update Satellite model to print name instead of object
- Create moon as satellite of earth

::

    pip install ipython
    make shell

::

    from planets import models
    earth = models.Planet.create(name="Earth", mass=100.0)
    moon = models.Satellite.create(name="Moon", mass=25.0, planet=earth)

Use administration GUI
----------------------

- create mars as Planet.create(name="Mars", mass="")
- alter Planet and Satellite to display name

Inspect ``models/__init__.py``
-----------------------

- 

Inspect ``__init__.py``
-----------------------

- uses familiar create_app style
- dwell upon blueprints facet
- dwell upon administration facet
- make REST API support name instead of ID
- query from command line with curl
