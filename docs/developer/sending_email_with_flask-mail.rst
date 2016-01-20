Sending Email with Flask-Mail
=============================

Lots of applications need to send emails in the course of their operation.  Email remains one of the best sources of *identity* on the Internet today.  `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_ is an easy way to integrate email-sending capabilities into your application.

Configuration
-------------

By default, :class:`flask_diamond.ext.email` is already enabled in :func:`flask_diamond.Diamond.init_app`, so there is nothing special to do.  The project created by ``diamond-scaffold.sh`` has email commented out by default, so you will have to enable this in your project's ``__init__.py`` file.

The settings for the SMTP server are located in your configuration file.  The relevant lines are these:

::

    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

You will need to set this configuration based on your particular email setup.

SMTP Server
-----------

In order for your application to be able to send emails, you will need access to an `SMTP server <https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>`_.  It is possible to use an email provider such as Gmail, but be aware that you won't be able to route a very high volume of email through a service like that.  Often times, you can use a web hosting provider for higher volumes.  Since every situation is different, you will need to track down your mail server configuration on your own.
