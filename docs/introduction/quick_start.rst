Quick Start
===========

Flask-Diamond installs in a Python environment with :doc:`virtualenv <../user/requirements_management_with_virtualenv>`.  Please see the :doc:`system_requirements` for information about installation pre-requisites.

Install Flask-Diamond
---------------------

Create a :doc:`virtualenv <../user/requirements_management_with_virtualenv>` for your new Flask-Diamond application, and then install Flask-Diamond with `pip <http://pip.readthedocs.org/en/latest/>`_.

::

    mkdir my-application
    cd my-application
    mkvirtualenv -a . my-application
    pip install Flask-Diamond

Scaffold a new Flask-Diamond application
----------------------------------------

Create a directory to hold your application, and then scaffold a new Flask-Diamond application inside that directory.  For this *Quick Start*, just use the default options.

::

    workon my-application
    flask-diamond scaffold app
    make install test

Use it!
-------

Create the database:

::

    make db

Start the server:

::

    make server

You now have a server running at http://127.0.0.1:5000.  Visit your new application in a web browser and login with the following account details:

- username: **admin@example.com**
- password: **the simple_password specified while scaffold the app**

Next Steps
----------

It's easy to scaffold a Flask-Diamond application.  Now you can :doc:`learn_flask_diamond` by reading the online materials.
