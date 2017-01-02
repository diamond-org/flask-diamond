Quick Start
===========

Flask-Diamond installs in a Python environment with :doc:`virtualenv <requirements_management_with_virtualenv>`.  Please see the :doc:`system_requirements` for information about installation pre-requisites.

Install Flask-Diamond
---------------------

Create a :doc:`virtualenv <requirements_management_with_virtualenv>` for your application and install Flask-Diamond.

::

    mkdir my-application
    cd my-application
    mkvirtualenv -a . my-application
    pip install Flask-Diamond

If any of these steps do not work, review the :doc:`system_requirements` and ensure everything is installed.

Scaffold a new Flask-Diamond application
----------------------------------------

Enter the virtual environment and scaffold a new Flask-Diamond application.  For this *Quick Start*, just use the default options.

::

    workon my-application
    flask-diamond scaffold app

Use it!
-------

Test the installation to ensure everything is installed correctly:

::

    make test

Create the application database:

::

    make db

Start the application server:

::

    make server

You now have a server running at http://127.0.0.1:5000. Depending on your OS, the following command will open your application in a browser.

::

    open http://localhost:5000

Login with the following account details:

- username: **admin@example.com**
- password: **the simple_password specified during scaffolding**

Next Steps
----------

Now that you have scaffolded your first Flask-Diamond application, you can read about how to :doc:`learn_flask_diamond` by using the online documentation and materials.
