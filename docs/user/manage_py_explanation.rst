``manage.py`` Explanation
=========================

Many applications will want to expose some functionality through a command line interface, and ``bin/manage.py`` provides an easy way to accomplish this.  For example:

- certain administrative tasks could be triggered from the command line
- other tasks can be automated using a tool like ``cron``

Many of the targets within the Flask-Diamond Makefile are actually wrappers for ``manage.py``, but you can invoke it manually on the command line like so:

::

    SETTINGS=$PWD/etc/conf/dev.conf bin/manage.py runserver

The following commands come with Flask-Diamond by default.

Commands
--------

- ``shell``: Launch the Python REPL (or iPython if installed) using `Flask-Script <http://flask-script.readthedocs.org/en/latest/>`_.  By default, the following objects will be imported into the namespace:

    - ``app``: your app's Flask-Diamond object
    - ``db``: your app's database object
    - ``user_datastore``: from `Flask-Security <https://pythonhosted.org/Flask-Security/>`_, this is the datastore containing all users

- ``runserver``: Launch your application's HTTP server.  When ``runserver`` is invoked, it will bind to ``localhost``.  The ``PORT`` your application listens on is defined in the :doc:`configuration_explanation`.

- ``publicserver``: Like ``runserver`` but public.  This causes the server to bind to ``0.0.0.0`` so that remote hosts can connect to your application.  This is intended for development purposes, and is not recommended for deployment.  See :doc:`web_service_with_wsgi` for more information about running a public web service.

- ``db``: This command acts as the entry point for `Flask-Migrate <http://flask-migrate.readthedocs.org/en/latest/>`_.  The subcommands available, taken directly from the command output, are:

    - ``upgrade``: Upgrade to a later version
    - ``heads``: Show current available heads in the script directory
    - ``show``: Show the revision denoted by the given symbol.
    - ``migrate``: Alias for 'revision --autogenerate'
    - ``stamp``: 'stamp' the revision table with the given revision; don't run any migrations
    - ``current``: Display the current revision for each database.
    - ``merge``: Merge two revisions together. Creates a new migration file
    - ``init``: Generates a new migration
    - ``downgrade``: Revert to a previous version
    - ``branches``: Show current branch points
    - ``history``: List changeset scripts in chronological order.
    - ``revision``: Create a new revision file.

- ``useradd``: Add a user to the users database via `Flask-Security <https://pythonhosted.org/Flask-Security/>`_.  This accepts the following arguments:

    - ``email``: (required)
    - ``password``: (required)
    - ``admin``: *True/False* Should this user have the *Admin* role?

- ``userdel``: Delete a user from the users database.

- ``init_db``: Drop the existing database using `Flask-SQLAlchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_ and re-create it.  This obviously destroys anything in the database, resetting it to its original state.

- ``populate_db``: Sometimes, it is convenient to populate the database with a starting set of objects.  The ``populate_db`` command is a handy opportunity to ship some data with your project.
