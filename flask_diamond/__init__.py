# -*- coding: utf-8 -*-
# Ian Dennis Miller

import logging
from flask.ext.security.signals import user_registered
from flask.ext.security import SQLAlchemyUserDatastore

from .utils.wtfhelpers import add_helpers

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

from flask.ext.admin import Admin
admin = Admin()

from flask.ext.mail import Mail
mail = Mail()


class Diamond(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app=None):
        if app is None and self.app is None:
            self.app = flask.Flask(
                __name__,
                static_folder='views/static',
                template_folder='views/templates'
            )
        elif app:
            self.app = app

        # configure the application
        self.config()
        self.logs()

        # setup database
        self.database()

        # setup components, referring out to our pre-allocated globalish objects
        self.ext_security()
        self.administration()
        self.wtforms()
        self.email()
        self.blueprints()
        self.webassets()
        self.debugtoolbar()
        self.signals()
        self.error_handlers()
        self.request_handlers()

        if hasattr(self.app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'diamond'):
            pass
            #ctx.sqlite3_db.close()

    def config(self):
        "Establish configuration"
        self.app.config.from_envvar('SETTINGS')

    def logs(self):
        "init logging"
        handler = logging.FileHandler(self.app.config['LOG'])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        self.app.logger.addHandler(handler)
        if self.app.config.get("LOG_LEVEL") == "DEBUG":
            self.app.logger.setLevel(logging.DEBUG)
        elif self.app.config.get("LOG_LEVEL") == "WARN":
            self.app.logger.setLevel(logging.WARN)
        else:
            self.app.logger.setLevel(logging.INFO)
        self.app.logger.info('Startup with log: %s' % self.app.config['LOG'])

    def blueprints(self):
        "Setup blueprints"
        pass

    def webassets(self):
        "setup web assets"
        assets.init_app(self.app)

    def administration(self, index_view=None):
        from . import administration, models
        admin = Admin(
            name=self.app.config["PROJECT_NAME"],
            base_template='login_base.html',
            index_view=index_view or administration.ForceLoginView(name="Home")
        )
        admin.add_view(administration.UserView(models.User, db.session, category="Admin"))
        admin.add_view(administration.AdminModelView(models.Role, db.session, category="Admin"))
        admin.init_app(self.app)
        return admin

    def ext_security(self, **kwargs):
        "Setup Flask-Security"
        from . import models
        user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
        security.init_app(self.app, datastore=user_datastore, **kwargs)
        security._state = self.app.extensions["security"]
        security.datastore = user_datastore

    def database(self):
        "set up the database"
        db.app = self.app
        db.init_app(self.app)

    def email(self):
        "set up flask-mail"
        mail.init_app(self.app)

    def wtforms(self):
        "WTForms helpers"
        add_helpers(self.app)

    def debugtoolbar(self):
        "Enable the DebugToolbar"
        if 'DEBUG_TOOLBAR' in self.app.config and self.app.config['DEBUG_TOOLBAR']:
            toolbar.init_app(self.app)

    def error_handlers(self):
        import flask.ext.security as security

        @self.app.errorhandler(403)
        def page_not_found(e):
            if security.current_user.is_authenticated():
                return flask.redirect(flask.url_for("admin.index"))
            else:
                return flask.redirect(security.url_for_security("login"))

    def request_handlers(self):
        @self.app.route('/')
        def index():
            "set up the default handler for requests to /"
            return flask.redirect(flask.url_for("admin.index"))

    def signals(self):
        @user_registered.connect_via(self.app)
        def user_registered_sighandler(sender, **extra):
            "add User role to all self-registration users"
            user_role = security.datastore.find_role("User")
            security.datastore.add_role_to_user(extra['user'], user_role)
            self.logger.info("added role User to %s" % extra['user'])

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
