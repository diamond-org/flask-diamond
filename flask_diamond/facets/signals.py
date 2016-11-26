# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask_security.signals import user_registered
from .accounts import security
from .database import db


def init_signals(self):
    """
    Initialize Flask signal handlers

    :returns: None

    Flask provides a number of signals corresponding to things that happen
    during the operation of the application, which can also be thought of
    as events.  It is possible to create signal handlers that will respond
    to these events with some behaviour.
    """
    @user_registered.connect_via(self.app)
    def user_registered_sighandler(sender, **extra):
        "add User role to all self-registration users"
        user_role = security.user_datastore.find_role("User")
        security.user_datastore.add_role_to_user(extra['user'], user_role)
        db.session.commit()
        self.app.logger.info("added role User to %s" % extra['user'])
