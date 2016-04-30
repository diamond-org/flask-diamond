# -*- coding: utf-8 -*-
# Ian Dennis Miller

import flask
from .ext import *

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

application = None


class Diamond:
    """
    A Diamond application.

    :param app: a Flask app that you created on your own
    :type app: Flask
    :returns: None
    """

    def __init__(self, name=None):
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

        if hasattr(self.app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

    def bootup(self, extension_name, **kwargs):
        """
        initialize an extension
        """
        init_method = "init_{0}".format(extension_name)
        if not hasattr(self, init_method):
            method_to_call = globals()[init_method]
        else:
            method_to_call = getattr(self, init_method)
        setattr(self, init_method, method_to_call)

        try:
            # try to explicitly pass self as the first parameter
            result = method_to_call(self, **kwargs)
        except TypeError:
            # just call it because it will be wrapped to inject self
            result = method_to_call(**kwargs)

        self.app.logger.debug("bootup {0}".format(extension_name))
        return result

    def super(self, extension_name, **kwargs):
        """
        invoke the initialization method for the superclass

        ex: self.super("administration")
        """

        init_method = "init_{0}".format(extension_name)
        # ensure the global version is called
        method_to_call = globals()[init_method]
        result = method_to_call(self, **kwargs)
        return result

    def teardown(self, exception):
        """
        Remove any persistent connections during application context teardown.

        :returns: None
        """

        ctx = stack.top
        if hasattr(ctx, 'diamond'):
            pass
            # ctx.sqlite3_db.close()

    def init_accounts(self):
        "initialize accounts with the User and Role classes imported from .models"
        from .models.user import User
        from .models.role import Role
        self.super("accounts", user=User, role=Role)

    def init_administration(self):
        "Initialize admin interface"
        from .models.user import User
        from .models.role import Role
        self.super("administration", user=User, role=Role)

    @property
    def _app(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'app'):
                pass
            return ctx.app


def create_app():
    global application
    if not application:
        application = Diamond()
        application.bootup("configuration")
        application.bootup("logs")
        application.bootup("database")
        application.bootup("marshalling")
        application.bootup("accounts")
        application.bootup("blueprints")
        application.bootup("signals")
        application.bootup("forms")
        application.bootup("error_handlers")
        application.bootup("request_handlers")
        application.bootup("administration")
        # application.bootup("rest")
        # application.bootup("webassets")
        # application.bootup("email")
        # application.bootup("debugger")
        # application.bootup("task_queue")

    return application.app
