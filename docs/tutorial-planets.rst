Planets Tutorial
================

The Planets Tutorial will introduce Flask-Diamond by demonstrating a simple web application that manages Planets and Satellites in a database.
When you are done with this tutorial, you will understand a powerful pattern for using Flask-Diamond to develop applications.
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

During the tutorial, we will accomplish the following:

1. Scaffold a working "Planets" application
2. Use the application to create a few Planets and Moons in the application database
3. Alter the Model code to make the GUI behave differently
4. Introduce several important files that are used to structure a Flask-Diamond application

Setup for Tutorial
------------------

The following commands will prepare you to begin the tutorial:

::

    mkdir planets
    cd planets
    mkvirtualenv -a . planets
    pip install Flask-Diamond ipython
    flask-diamond scaffold app

For a more detailed explanation of these commands, please see the :doc:`quick-start`.
When you run ``flask-diamond scaffold app``, you will be prompted to answer some questions.
Give your application and module the name of ``planets`` during scaffolding.
For all other questions, you can accept the default answers by pressing Enter for each question.

Tutorial Exercises
------------------

Now, we'll use a special scaffold called ``tutorial-planets`` for the rest of this tutorial.
The ``tutorial-planets`` scaffold places some example models and views into the application structure.

::

    flask-diamond scaffold tutorial-planets
    make test db server
    open http://localhost:5000

Your web browser should now display the ``planets`` application.
If you ran into problems, please review the :doc:`quick-start` to ensure you have all the requirements installed and working.

The Planets application comes with two object classes:

1. *Planets*, which are large celestial bodies that orbit something like a star
2. *Satellites*, which are little bodies orbiting planets

We will use these classes to model our solar system.

Create Planet Earth
^^^^^^^^^^^^^^^^^^^

The first thing to do is enter the application shell.
The ``make shell`` command enters the application context, connects to the database, and starts an interactive shell that will allow us to interact with our application.

::

    make shell

Enter the following commands to create Earth.

::

    from planets import models
    earth = models.Planet.create(name="Earth", mass=100.0)

We have provided two parameters to the Planet.create method: *name* and *mass*.
These model parameters come from the Planet model class definition, which we will investigate in the next section.

Also create Earth's lunar body, the Moon.

::

    moon = models.Satellite.create(name="Moon", mass=25.0, planet=earth)

Take note of the additional parameter: *planet*.
The application database now contains the Earth and the Moon.

Inspect Models
^^^^^^^^^^^^^^

Using a text editor, inspect the files in ``planets/models``.

- ``__init__.py`` proxies all model classes
- ``Planet.py`` contains definition of Planet class
- ``Satellite.py`` contains definition of Satellite class

The *Planet* model enables us to capture the name and mass of a planet in the application database.
The *Satellite* model is similar to the Planet model, but it also includes a foreign key relationship so that satellites may belong to planets.
See :doc:`models` for more about how to write model classes.

Administration GUI
^^^^^^^^^^^^^^^^^^

**Log in to GUI**

Using a web browser, connect to the application server in a new tab.
If you used the default scaffolding settings, your application server is online at http://localhost:5000/.

First, log in as ``admin@example.com`` using randomly generated password.
The development password can be recovered from ``Makefile``.

**Create Mars**

Now that you have logged in, create a new Planet called Mars using the GUI.
Choose *Admin* from the drop-down menu at the top of the screen.
Select the *Planet* model from the menu.
Once the Planets List View has loaded, click *Create* to make a new planet.
Use the following values:

- name: Mars
- mass: 90.0

**Create Phobos**

Repeat this process to create a new Satellite using the menus.

- name: Phobos
- mass: 10.0
- planet: Mars

However, you will run into trouble when you try to set the planet to Mars.
To fix this, open the file ``models/planet.py``.
Add a function called ``__str__`` within the Planet class:

::

    def __str__(self):
        return self.name

With the string representation function in place, try to create Phobos again.
You will now be able to select *Mars* from the drop-down.

Inspect ``__init__.py``
^^^^^^^^^^^^^^^^^^^^^^^

The last step in this tutorial is to look at the most important file of all, ``__init__.py``, which controls every aspect of your application.
Using a text editor, inspect the file ``planets/__init__.py``.
Flask-Diamond applications mostly follow Flask's ``create_app()`` pattern.
If you are not yet familiar with Flask applications, read :doc:`writing-an-application`.

**blueprints facet**

Take a look at ``init_blueprints``, which registers two blueprints that provide basic administrative functionality to your application.
To add new views to your application, you will extend this function to register your own blueprints.

**administration facet**

Finally, look at ``init_administration``, which adds a ``ModelView`` for Planets and Satellites.
When you create new models in your application, if you wish to edit those models using the GUI, you will need to add those new models to ``init_administration``.

Tutorial Conclusion
^^^^^^^^^^^^^^^^^^^

To recap this tutorial, we covered the following:

- scaffold a new application
- use data model to create objects in our database
- use web GUI to create even more objects
- edit the data model code to add functionality
- inspect ``__init__.py`` to learn how applications are controlled

These fundamental ideas are common to many applications.
Of course, this tutorial is just an introduction.
Each of these topics has many more readings that will help you learn to master the facets of your application.

Next steps
----------

- :doc:`facets` describes the use of Flask-Diamond's *facets* for customizing your application's behavior.
- :doc:`writing-an-application` provides examples and describes an approach for designing and programming an application that achieves your goals.
- :doc:`model-view-controller` is a more advanced document that describes the Flask-Diamond architecture.  Model-View-Controller (MVC) is widely used in software engineering to write applications that provide a user interface.  Once you understand how to implement MVC using Flask-Diamond, you will be able to write applications for a wide range of domains.
