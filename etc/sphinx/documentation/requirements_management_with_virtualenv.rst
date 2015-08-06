Requirements Management with virtualenv
=======================================

The preferred way to manage your Python requirements is with virtualenv.  The preferred way to manage virtualenvs is with virtualenvwrapper, which provides a regularized interface for creating and using virtualenvs.

When you install your Flask-Diamond application inside a virtualenv, you are able to "freeze" the state of your installed Python libraries.  This way, your application will never suffer from broken requirements due to a system-wide upgrade.  This document describes the typical workflow for using virtualenv to manage a Flask-Diamond project.

Pre-requisites
--------------

You need to install the minimum :doc:`../introduction/system_requirements` in order to have the necessary tools for this process.  It is assumed that you now have ``workon`` and ``mkvirtualenv`` available.  If you cannot call these commands in a terminal, then you should double-check your :doc:`../introduction/system_requirements`.

Making a New virtualenv
-----------------------

The way to initialize a new virtualenv is with ``mkvirtualenv``, which is described on the `mkvirtualenv documentation <http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#mkvirtualenv>`_.  The following example demonstrates creating a virtualenv called *my-diamond-app*.

::

    $ mkvirtualenv my-diamond-app
    New python executable in my-diamond-app/bin/python2.7
    Also creating executable in my-diamond-app/bin/python
    Installing setuptools, pip...done.
    (my-diamond-app) $

Upon creating the virtualenv, it will be activated and your shell prompt changes to include your project name as a prefix.  You can verify that you are inside the virtualenv by echoing an environment variable to the screen:

::

    (my-diamond-app) $ echo $VIRTUAL_ENV
    ~/.virtualenvs/my-diamond-app

Using it
--------

When you need to work on your project, you must activate your project's virtualenv using ``workon``.  After calling ``workon``, your shell's search path will be updated so that scripts from your virtualenv will be called before any globally installed scripts.

::

    $ workon my-diamond-app
    (my-diamond-app) $

In order to leave the virtualenv and return to a normal shell, use ``deactivate``.

::

    (my-diamond-app) $ deactivate
    $

pip and Installation
--------------------

When you use ``pip`` inside your virtualenv, it will automatically install packages locally, instead of installing them at the system level.  This way, it's easy to install anything without needing root access.  In the following example, we are inside our virtualenv and we want to upgrade pip:

::

    (my-diamond-app) $ pip install --force -U pip
    Collecting pip
      Downloading pip-7.1.0-py2.py3-none-any.whl (1.1MB)
        100% |████████████████████████████████| 1.1MB 172kB/s
    Installing collected packages: pip
    Successfully installed pip-7.1.0
    (my-diamond-app) $

Freezing Python Requirements
----------------------------

``pip`` provides a handy mechanism for printing all of the installed libraries, along with their versions.  When called within your virtualenv, it produces a snapshot of all your project requirements so you can easily re-install them later.

::

    (my-diamond-app) $ pip freeze
    Jinja2==2.7.3
    MarkupSafe==0.23
    mr.bob==0.1.1
    requests==2.7.0
    virtualenv==1.11.6
    virtualenvwrapper==4.2
    (my-diamond-app) $

You can also store your requirements in a requirements file.

::

    (my-diamond-app) $ pip freeze > requirements.txt


Makefile support
----------------

By default, Flask-Diamond provides ``make install``, which will use requirements.txt to install your project's pre-requisites automatically.
