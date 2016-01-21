Debugging a Flask-Diamond Application
=====================================

To simplify debugging, Flask-Diamond provides a basic setup for logging so that your application can write trace data to a file for your inspection.  Flask-Diamond also integrates `Flask-DebugToolbar <http://flask-debugtoolbar.readthedocs.org/en/latest/>`_ to provide a powerful debugger shell directly in the interface.

Logs
----

Flask-Diamond creates a logging object during initialization.  You can write log messages to this object with the following basic code:

::

    flask.current_app.logger.debug("this is a debug-level message")

    flask.current_app.logger.warn("important! this is a warning message")

The destination for log files is controlled in the configuration file.  During development, ``dev.conf`` will write log messages to the var/logs path of your project.

Log Level
^^^^^^^^^

During debugging, it is sometimes useful to get extra information about your application while it is running.  The *log level* is used to control how critical logging is.  When the level is ``DEBUG``, then all messages are printed - this can be verbose.  When the level is ``INFO``, then debugging messages are not printed at all, but general information messages are.  When the level is ``WARN``, then only important messages are printed.  This level may be suitable for production.

DebugToolbar
------------

`Flask-DebugToolbar <http://flask-debugtoolbar.readthedocs.org/en/latest/>`_ is a useful web gadget that can help developers to diagnose problems within the browser.  In practice, you may end up doing most of your development in a terminal, but the Debug Toolbar can nevertheless be handy for casual projects.

In the application configuration file, whenever ``DEBUG=True`` the DebugToolbar will be active.  By default, the development configuration enables debugtoolbar whereas the production configuration disables it.  It is possible to completely remove the DebugToolbar by ensuring the ``debugger`` extension is not loaded at all during :func:`flask_diamond.Diamond.init_app()`.
