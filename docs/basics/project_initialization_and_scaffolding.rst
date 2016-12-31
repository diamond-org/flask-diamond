:tocdepth: 2

Project Initialization and Scaffolding
======================================

The quickest way to start a new Flask-Diamond project is to use the scaffolding system.  Scaffolding applies a series of file templates that result in a starter application that can be further customized.  This document discusses the configuration questions that are used during scaffolding.

As described in the :doc:`../introduction/quick_start`, the basic process looks like this:

::

    mkdir my-application
    cd my-application
    mkvirtualenv -a . my-application
    pip install Flask-Diamond
    flask-diamond scaffold app
    make install docs test db server

About Scaffolding
-----------------

When you invoke ``flask-diamond``, a template is automatically applied.  Using `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_, a brief set of questions are used to populate the templates with variables.  When you answer these questions, your choices are stored in a file called ``.mrbob.ini`` that is located in the root folder of your project.

Template questions
------------------

This template is suitable for supporting many types of Python projects.  It will create a basic directory structure that provide requirements management, documentation, build, deployment, and other basic project needs.  This step of the scaffolding process asks the following questions:

1. What is the name of the application (i.e. username, daemon name, etc)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``Flask-Diamond``

The application name is a human-readable name that will be used in documentation, on websites, and when talking about the project.  This should follow conventions that are established within your community.  In the case of **Flask-Diamond**, the project name tries to follow the naming pattern established by other Flask extensions like `Flask-Admin <http://flask-admin.readthedocs.org/en/latest/>`_, `Flask-Security <http://pythonhosted.org/Flask-Security/>`_, and `Flask-RESTful <http://flask-restful.readthedocs.org/en/0.3.4/>`_.

2. What is the name of the module (can be different from the application name)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``flask_diamond``

The module name is a `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ styled name.  In the case of Flask-Diamond, the module name should be lowercase and hyphens become underscores.  Thus, Flask-Diamond becomes **flask_diamond**.

3. What is the short description for this project?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``Flask-Diamond is a batteries-included Flask framework.``

This question corresponds to the ``setuptools.setup(description="")`` variable in the project setup.py file.  The short description is intended to appear as a brief summary in `PyPI <https://pypi.python.org/pypi>`_.

4. What is the long description for this project?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``Flask-Diamond is a batteries-included Flask framework. Easily scaffold a working application with sensible defaults, then override the defaults to customize it for your goals.``

This question corresponds to the ``setuptools.setup(long_description="")`` variable in the project setup.py file.  In practice, this usually ends up being multiple paragraphs.

5. Who is the author of this software?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``Ian Dennis Miller``

This question corresponds to the ``setuptools.setup(author="")`` variable in the project setup.py file.  It's a name.  Your name.

6. What is the author's contact email?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``iandennismiller@gmail.com``

This question corresponds to the ``setuptools.setup(author_email="")`` variable in the project setup.py file.  This is your public contact information.

7. What is the author's contact URL?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``http://flask-diamond.org``

This question corresponds to the ``setuptools.setup(url="")`` variable in the project setup.py file.  If you have a website that provides support for your project, put it here.  In the case of Flask-Diamond, there are lots of resources on the official website, including a link to the project issue tracker.  As a result, Flask-Diamond uses the project URL as the contact URL.

8. Which port will the daemon listen on?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``5000``

Your application will run as an HTTP service that listens on the port provided here.
Thus, if you answer ``8000`` you will be able to connect to your application at ``http://localhost:8000/admin``.

Automatically generated scaffolding fields
------------------------------------------

There are some steps in the scaffolding process that are automatically generated for you because they involve random processes.

1. What is the secret key?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``\x83.RH\xdc@\x0fu\xb5o\xcd\xf5\xc4\xd5\xb12\xc2M\xca\x96\xc8\xbf\xeb\xde``

Flask uses a secret key to seed certain cryptographic functions.  To generate a suitable random string for the secret key, use the following Python code:

::

    python -c 'import os; print(repr(os.urandom(24)))'

2. What is the hash_salt?
^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``t52ybrp0oOGHkQEZ``

Flask uses a hash salt for password storage.  To generate a suitable random string for the hash salt, use the following Python code:

::

    python -c 'import string as s, random as r; \
        print repr("".join(r.choice(s.letters+s.digits) for _ in range(16)))'


3. What is the simple_password?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``abc``

Flask-Diamond can simplify the creation of testing accounts during development.
One of the default accounts has administrative privileges, so a simple password is used to protect the account.
This password is just 3 letters long by default, so it should never be used anywhere but during development.
To ensure this weak password is not used in production, the ``Makefile`` is hardcoded to use the development configuration, only.
