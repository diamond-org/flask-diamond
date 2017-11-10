System Requirements
===================

Flask-Diamond requires some software to be installed in order to function.  Once you have installed these requirements, you can follow the :doc:`quick-start` to start your first project.  The following packages should be installed globally, as the superuser, for all users on the system to access.

- `Python 2.7.x <https://www.python.org/download/releases/2.7/>`_ or `3.4 and above <https://www.python.org/download/releases/3.4.0/>`_.
- Python development libraries (i.e. header files for compiling C code)
- `pip <http://pip.readthedocs.org/en/latest/>`_
- `virtualenv <http://virtualenv.readthedocs.org/en/latest/>`_
- `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_

The following sections describe the process for installing these requirements on various systems.  In each of the following examples, it is assumed you will be using a root account (or some other privileged account).

If you do not have root access, then refer to the section :ref:`unprivileged-installation` for information about creating a virtualenv in your user account.

Debian/Ubuntu
-------------

Flask-Diamond installs cleanly on Debian and Ubuntu systems released after 2011.

::

    apt-get install python python-dev python-pip build-essential
    apt-get install sqlite-dev
    pip install --upgrade pip
    pip install --upgrade virtualenv
    pip install virtualenvwrapper

Redhat
------

Flask-Diamond can be installed on RedHat, but ensure your package manager is installing Python 2.7; as of August 2015, RHEL provides an older version.

::

    yum install python python-devel python-pip
    yum install sqlite-devel
    pip install --upgrade pip
    pip install --upgrade virtualenv
    pip install virtualenvwrapper

OSX with Homebrew
-----------------

Flask-Diamond installs pretty easily on OSX with Homebrew.  Make sure you are using the *admin* user for this process, just like a normal Homebrew operation.

::

    brew install python --universal --framework
    brew install pyenv-virtualenv
    brew install pyenv-virtualenvwrapper
    brew install sqlite
    pip install --upgrade pip

Windows
-------

First, install Python from https://www.python.org/downloads/windows/.
Then, launch PowerShell and gain administrative privileges.
Finally, use `pip` to perform a site-wide install of several core libraries.

::

    start-process powershell –verb runAs
    pip install virtualenvwrapper
    pip install virtualenvwrapper-win
    pip install pyreadline

Windows installation of Flask-Diamond is similar to UNIX:

::

    cmd.exe
    mkvirtualenv my-app
    workon my-app
    pip install Flask-Diamond
    easy_install -U mr.bob==0.1.1
    pip install --no-deps Flask-Diamond

Discussion of Windows 10 installation is ongoing here: https://github.com/diamond-org/flask-diamond/issues/8

.. _unprivileged-installation:

Unprivileged Installation
-------------------------

Sometimes, you do not have root access to the system.  It is still possible to use Flask-Diamond, but the installation process is slightly different because it does not use virtualenvwrapper.  Instead, you will create your virtualenv directly and use the `activate` macro to work on it.

::

    curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    python virtualenv.py my-diamond-app
    source my-diamond-app/bin/activate
    pip install Flask-Diamond
