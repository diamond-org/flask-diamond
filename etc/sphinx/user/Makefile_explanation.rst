``Makefile`` Explanation
========================

The Makefile that ships with Flask-Diamond by default includes a number of targets that address several common tasks throughout the life cycle of a project.  The way to use the Makefile is with the ``make`` command.  Thus, to install the project with make, you'd invoke ``make install``.

During development, the Makefile is one of the primary ways for you to interact with your project.  You may find yourself running ``make db server`` or perhaps ``make single`` with some regularity.  It is recommended to become familiar with the Flask-Diamond Makefile.

Integration
-----------

These targets control project builds.

- ``install``: Use setup.py to install the project (typically inside a virtualenv).
- ``clean``: Delete all of the temporary files created by ``install``.
- ``docs``: Use `Sphinx <http://sphinx-doc.org/>`_ to render the documentation in ``etc/sphinx``.

Development
-----------

These targets are used to run the application with the ``dev.conf`` profile.

- ``server``: Invoke the HTTP server in debug mode with ``dev.conf``
- ``shell``: Enter a python (or ipython) shell within the virtualenv.
- ``notebook``: Use ipython notebook, if installed, to inspect the application.

Testing
-------

These targets are used to run automated tests.

- ``test``: Run all of the tests using nosetests.
- ``single``: Run only tests marked with the ``@attr("single")`` decorator.
- ``watch``: Enter a loop that watches for any project source code to be changed, and then automatically run any tests marked with the ``@attr("single")`` decorator.

Databases
---------

These targets control the database.  By default these use the ``dev.conf`` profile so as to avoid inadvertently changing the production database.

- ``db``: drop the database, re-create the database, and populate the database with starter values.
- ``migratedb``: when the data model schema has changed, use ``migratedb`` to create a new data migration.
- ``upgradedb``: apply all data migrations, in order, until the database is up to date.
