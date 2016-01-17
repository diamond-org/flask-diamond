# -*- coding: utf-8 -*-
# Ian Dennis Miller

import flask
from .ext import *

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Diamond(object):
    """
    A Diamond application.

    :param app: a Flask app that you created on your own
    :type app: Flask
    :returns: None
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, name=None, extensions=["email", "task_queue", "request_handlers"]):
        """
        Initialize a Diamond application.

        :param app: a Flask app that you created on your own
        :type app: Flask
        :returns: Flask -- the initialized application object

        This function is the backbone of every Diamond application.  It will
        initialize every component of the application.  To control the
        behaviour of the initialization process, override these functions
        within your own application.
        """

        if not name:
            name = __name__

        self.app = flask.Flask(name)
        extension_list = [
            "configuration",
            "logs",
            "database",
            "accounts",
            "administration",
            "forms",
            "webassets",
            "debugger",
            "rest",
            "blueprints",
            "signals",
            "error_handlers",
        ]
        extension_list.extend(extensions)

        for extension_name in extension_list:
            init_method = "init_{0}".format(extension_name)
            if not hasattr(self, init_method):
                method_to_call = globals()[init_method]
            else:
                method_to_call = getattr(self, init_method)
            result = method_to_call(self)

        if hasattr(self.app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

    def teardown(self, exception):
        """
        Remove any persistent connections during application context teardown.

        :returns: None
        """

        ctx = stack.top
        if hasattr(ctx, 'diamond'):
            pass
            # ctx.sqlite3_db.close()

    @property
    def _app(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'app'):
                pass
            return ctx.app


def create_app():
    diamond = Diamond()
    diamond.init_app()
    return diamond.app
