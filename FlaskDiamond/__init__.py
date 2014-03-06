# -*- coding: utf-8 -*-
# Ian Dennis Miller

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# these "globalish" objects need to be set up before create_app so they will be scoped correctly
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()

from flask.ext.security import Security
security = Security()

def create_app():
    from .Startup import Startup
    startup = Startup(db, security, toolbar)
    return startup.get_app()
