# -*- coding: utf-8 -*-
# Ian Dennis Miller

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import flask
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

from flask.ext.assets import Environment
assets = Environment()

class Diamond(object):
    def __init__(self, _db, _security_obj, _toolbar, app=None):
        db = _db
        security_obj = _security_obj
        toolbar = _toolbar
        self.db = db
        self.security_obj = security_obj
        self.toolbar = toolbar
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app=None):
        if app is None and self.app is None:
            self.app = flask.Flask(__name__, static_folder='views/static', template_folder='views/templates')
        elif app:
            self.app = app
        # configure the application
        self.config(self.app)
        self.logger(self.app)

        # setup database
        self.database(self.app, self.db)

        # setup components, referring out to our pre-allocated globalish objects
        self.security(self.app, self.db, self.security_obj)
        self.administration(self.app, self.db)
        self.wtforms(self.app)
        self.email(self.app)
        self.blueprints(self.app)
        self.webassets(self.app)
        self.debugtoolbar(self.app, self.toolbar)
        self.signals(self.app, self.security)
        self.error_handlers(self.app)
        self.request_handlers(self.app)

        if hasattr(self.app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'diamond'):
            pass
            #ctx.sqlite3_db.close()

    def config(self, app):
        "Establish configuration"
        app.config.from_envvar('SETTINGS')

    def logger(self, app):
        "init logging"
        import logging
        handler = logging.FileHandler(app.config['LOG'])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.INFO)
        app.logger.debug('Startup with log: %s' % app.config['LOG'])

    def blueprints(self, app):
        "Setup blueprints"
        pass

    def webassets(self, app):
        "setup web assets"
        assets.init_app(app)

    def administration(self, app, db):
        from . import administration as Administration, models as Models
        admin = Administration.Admin(
            app,
            name=app.config["PROJECT_NAME"],
            base_template='login_base.html',
            index_view=Administration.ForceLoginView(name="Home")
            )
        admin.add_view(Administration.UserView(Models.User, db.session, category="Admin"))
        admin.add_view(Administration.AdminModelView(Models.Role, db.session, category="Admin"))
        return admin

    def security(self, app, db, security_obj):
        "Setup Flask-Security"
        from flask.ext.security import SQLAlchemyUserDatastore
        from . import models as Models

        user_datastore = SQLAlchemyUserDatastore(db, Models.User, Models.Role)
        security_obj.init_app(app, user_datastore)
        security_obj.datastore = user_datastore

    def database(self, app, db):
        "set up the database"
        db.app = app
        db.init_app(app)

    def email(self, app):
        "set up flask-mail"
        from flask_mail import Mail
        mail = Mail(app)
        self.mail = mail

    def wtforms(self, app):
        "WTForms helpers"
        from .utils.wtfhelpers import add_helpers
        add_helpers(app)

    def debugtoolbar(self, app, toolbar):
        "Enable the DebugToolbar"
        if 'DEBUG_TOOLBAR' in app.config and app.config['DEBUG_TOOLBAR']:
            toolbar.init_app(app)

    def error_handlers(self, app):
        import flask.ext.security as security

        @app.errorhandler(403)
        def page_not_found(e):
            if security.current_user.is_authenticated():
                return flask.redirect(flask.url_for("admin.index"))
            else:
                return flask.redirect(security.url_for_security("login"))

    def request_handlers(self, app):
        @app.route('/')
        def index():
            "set up the default handler for requests to /"
            return flask.redirect(flask.url_for("admin.index"))

    def signals(self, app, security_obj):
        import flask, logging
        from flask.ext.security.signals import user_registered

        @user_registered.connect_via(app)
        def user_registered_sighandler(sender, **extra):
            "add User role to all self-registration users"
            user_role = security_obj.datastore.find_role("User")
            security_obj.datastore.add_role_to_user(extra['user'], user_role)
            logging.getLogger("flask-diamond").info("added role User to %s" % extra['user'])

    @property
    def _app(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'app'):
                pass
            return ctx.app

def create_app():
    diamond = Diamond(db, security, toolbar)
    diamond.init_app()
    return diamond.app
