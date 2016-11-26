# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import flask


def init_error_handlers(self):
    """
    Initialize handlers for HTTP error events

    :returns: None

    Flask is able to respond to HTTP error codes with custom behaviours.
    By default, it will redirect error 403 (forbidden) to the login page.
    """
    import flask_security as security

    @self.app.errorhandler(403)
    def page_forbidden(e):
        if security.current_user.is_authenticated:
            return flask.redirect(flask.url_for("admin.index"))
        else:
            return flask.redirect(security.url_for_security("login"))


def init_request_handlers(self):
    """
    request handlers

    :returns: None

    Flask handles requests for URLs by scanning the URL path.  Typically,
    any serious functionality will be collected into Views.  However, this
    function is a chance to define a few simple utility URLs.

    If in your application you want to disable the default handlers in
    Flask-Diamond, you can override them like this.

    >>> def request_handlers(self):
    >>>     pass
    """
    @self.app.route('/')
    def index():
        "set up the default handler for requests to /"
        return flask.redirect(flask.url_for("admin.index"))
