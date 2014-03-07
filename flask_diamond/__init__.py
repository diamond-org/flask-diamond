# -*- coding: utf-8 -*-
# Ian Dennis Miller

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

# these "globalish" objects need to be set up before create_app so they will be scoped correctly
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()

from flask.ext.security import Security
security = Security()

class Diamond(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def create_app():
        from .Startup import Startup
        startup = Startup(db, security, toolbar)
        return startup.get_app()

def create_app():
