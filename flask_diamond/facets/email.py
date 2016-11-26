# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_mail import Mail

mail = Mail()


def init_email(self):
    """
    Initialize email facilities.

    :returns: None

    `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_ is a
    useful tool for creating and sending emails from within a Flask application.
    There are a number of configuration settings beginning with ``MAIL_``
    that permit control over the SMTP credentials used to send email.
    """

    mail.init_app(self.app)
