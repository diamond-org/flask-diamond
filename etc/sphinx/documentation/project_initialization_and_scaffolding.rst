:tocdepth: 2

Project Initialization and Scaffolding
======================================

The quickest way to start a new Flask-Diamond project is to use the scaffolding system.  Scaffolding applies a series of file templates that result in a starter application that can be further customized.  This document discusses the configuration questions that are used during scaffolding.

As described in the :doc:`../introduction/quick_start`, the basic process looks like this:

1. Install Flask-Diamond in a virtualenv

::

    mkvirtualenv my-diamond-app
    pip install Flask-Diamond

2. Scaffold an application in a new directory

::

    mkdir my-diamond-app
    cd my-diamond-app
    diamond-scaffold.sh

About Scaffolding
-----------------

When you invoke ``diamond-scaffold.sh``, two templates are downloaded and automatically applied:

- :ref:`diamond-project`
- :ref:`diamond-app`

Using `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_, a brief set of questions are used to populate the templates with variables.  When you answer these questions, your choices are stored in a file called ``.mrbob.ini`` that is located in the root folder of your project.

.. _diamond-project:

diamond-project
---------------

The first templates applied during scaffolding come from https://github.com/iandennismiller/diamond-project.  These templates are suitable for supporting many types of Python projects.  They will create a basic directory structure that provide requirements management, documentation, build, deployment, and other basic project needs.  This step of the scaffolding process asks the following questions:

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

8. What ssh key is used to deploy?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``~/.ssh/id_rsa``

This question corresponds to ``fabric.api.env.key_filename`` inside ``fabfile.py``, which is the SSH key filename that is used to deploy the project to a remote host via SSH.

9. Where is the git repository?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``https://github.com/iandennismiller/flask-diamond``

If you will be distributing your application through hosted version control, then provide the URL here.  This is used during deployment, and it is useful for reference.

.. _diamond-app:

diamond-app
-----------

The last templates applied during scaffolding come from https://github.com/iandennismiller/diamond-app.  These templates extend diamond-project with a fully-articulated Flask-Diamond application.  The questions during this portion of scaffolding pertain primarily to the configuration of the Flask project, itself.

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

3. Which port will the daemon listen on?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: ``5000``

Your application will run as an HTTP service that listens on the port provided here.  Thus, if you answer ``8000`` you will be able to connect to your application at ``http://localhost:8000/admin``.
