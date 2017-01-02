Libraries Included in Flask-Diamond
===================================

Flask-Diamond pulls from many different Flask extensions, which are all listed in this document.  A significant factor for inclusion with Flask-Diamond is the existence of good documentation.  Most of the following libraries therefore provide extensive documentation that can help you to understand everything in greater detail.

Database/Model
--------------

- `Flask-SQLAlchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_: "Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It requires SQLAlchemy 0.6 or higher. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks."
- `Flask-Migrate <http://flask-migrate.readthedocs.org/en/latest/>`_: "Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are provided as command line arguments for Flask-Script."
- `Flask-Marshmallow <http://flask-marshmallow.readthedocs.org/en/latest/>`_: "Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) integrates with Flask-SQLAlchemy."

Development
-----------

- `Flask-Testing <https://pythonhosted.org/Flask-Testing/>`_: "The Flask-Testing extension provides unit testing utilities for Flask."
- `Flask-DebugToolbar <http://flask-debugtoolbar.readthedocs.org/en/latest/>`_: "This extension adds a toolbar overlay to Flask applications containing useful information for debugging."
- `Flask-DbShell <https://github.com/ffeast/flask-dbshell>`_: "The extension provides facilites for implementing Django-like ./manage.py dbshell command"
- `Flask-Script <http://flask-script.readthedocs.org/en/latest/>`_: "The Flask-Script extension provides support for writing external scripts in Flask. This includes running a development server, a customised Python shell, scripts to set up your database, cronjobs, and other command-line tasks that belong outside the web application itself."

Security
--------

- `Flask-Security <https://pythonhosted.org/Flask-Security/>`_: "Flask-Security allows you to quickly add common security mechanisms to your Flask application."
- `Flask-Login <https://flask-login.readthedocs.org/en/latest/>`_: "Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time."

Doing Stuff
-----------

- `Flask-Celery-Helper <https://github.com/Robpol86/Flask-Celery-Helper>`_: "Celery support for Flask without breaking PyCharm inspections."
- `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_: "The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts."

Interfaces
----------

- `Flask-Admin <http://flask-admin.readthedocs.org/en/latest/>`_: "In a world of micro-services and APIs, Flask-Admin solves the boring problem of building an admin interface on top of an existing data model. With little effort, it lets you manage your web service’s data through a user-friendly interface."
- `Flask-RESTful <http://flask-restful.readthedocs.org/en/latest/>`_: "Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with your existing ORM/libraries. Flask-RESTful encourages best practices with minimal setup. If you are familiar with Flask, Flask-RESTful should be easy to pick up."
- `Flask-WTF <https://flask-wtf.readthedocs.org/en/latest/>`_: "Flask-WTF offers simple integration with `WTForms <http://wtforms.simplecodes.com/docs/>`_."

Presentation
------------

- `Flask-Assets <http://flask-assets.readthedocs.org/en/latest/>`_: "Flask-Assets helps you to integrate `webassets <http://webassets.readthedocs.org/en/latest/>`_ into your Flask application."
- `Flask-Markdown <http://pythonhosted.org/Flask-Markdown/>`_: "Flask-Markdown adds support for Markdown to your Flask application. There is little to no documentation for it, but it works just the same as markdown would normally."
