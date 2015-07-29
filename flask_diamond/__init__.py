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

from flask.ext.marshmallow import Marshmallow
ma = Marshmallow()

from flask.ext.restful import Api
rest = Api()

from flask.ext.celery import Celery
celery = Celery()


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

    def init_app(self,
            app=None,
            name=None,
            email=True,
            celery=True,
            request_handlers=True):

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

        if app is None and self.app is None:
            self.app = flask.Flask(
                name,
            )
        elif app:
            self.app = app

        # configure the application
        self.config()
        self.logs()

        # setup database
        self.database()

        # setup components, referring out to our pre-allocated globalish objects
        self.blueprints()
        self.wtforms()
        self.rest_api()
        self.webassets()
        self.debugtoolbar()
        self.signals()
        self.error_handlers()

        self.ext_security()
        self.administration()

        if email:
            self.email()

        if request_handlers:
            self.request_handlers()

        if celery:
            self.init_celery()

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
            #ctx.sqlite3_db.close()

    def config(self):
        """
        Load the application configuration from the ``SETTINGS`` environment variable.

        :returns: None

        ``SETTINGS`` must contain a filename that points to the configuration file.
        """

        self.app.config.from_envvar('SETTINGS')

    def logs(self):
        """
        Initialize a log file to collect messages.

        :returns: None

        This file may be written to using

        >>> flask.current_app.logger.info("message")
        """

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
        """
        Initialize blueprints.

        :returns: None

        By default, this function does nothing.  Your application needs to
        overload this function in order to implement your View functionality.
        More information about blueprints can be found in the
        `Flask documentation <http://flask.pocoo.org/docs/0.10/blueprints/>`_.
        """

        from views.diamond import diamond_blueprint
        self.app.register_blueprint(diamond_blueprint, url_prefix="/")

    def init_celery(self):
        """
        Initialize celery.
        """

        celery.init_app(self.app)

    def rest_api(self):
        """
        Initialize REST API.

        :returns: None

        By default, this function does nothing.  Your application needs to
        overload this function in order to implement your REST API.
        More information about REST can be found in the
        `documentation <http://flask-restful.readthedocs.org/en/latest/>`_.
        """

        rest.init_app(self.app)
        return rest

    def webassets(self):
        """
        Initialize web assets.

        :returns: None

        `webassets <https://github.com/miracle2k/webassets>`_ make it simpler
        to process and bundle CSS and Javascript assets.  This can be baked
        into a Flask application using
        `Flask-Assets <http://flask-assets.readthedocs.org/en/latest/>`_
        """

        assets.init_app(self.app)

    def administration(self, index_view=None, app_models=None):
        """
        Initialize the Administrative GUI.

        :param index_view: the View that will act as the index page of the admin GUI.
        :type index_view: AdminIndexView
        :returns: None

        The administration GUI is substantially derived from `Flask-Admin
        <http://flask-admin.readthedocs.org/en/latest/>`_. When this function
        is called, it will instantiate blueprints so the application serves
        the admin GUI via the URL http://localhost/admin.

        Typically, you will want to call this function even if you override
        it.  The following example illustrates using super() to invoke this
        administration() function from within your own application.

        >>> admin = super(MyApp, self).administration(
        >>>     index_view=MyApp.modelviews.RedirectView(name="Home")
        >>> )
        """

        from . import administration
        admin = Admin(
            name=self.app.config["PROJECT_NAME"],
            base_template='admin/login_base.html',
            index_view=index_view or administration.ForceLoginView(name="Home")
        )

        if not app_models:
            from . import models
        else:
            models = app_models

        admin.add_view(administration.UserView(models.User, db.session, category="Admin"))
        admin.add_view(administration.AdminModelView(models.Role, db.session, category="Admin"))

        admin.init_app(self.app)
        return admin

    def ext_security(self, app_models=None, **kwargs):
        """
        Initialize Security for application.

        :param kwargs: parameters that will be passed through to Flask-Security
        :type kwargs: dict
        :returns: None

        A number of common User account operations are provided by `Flask-
        Security <http://pythonhosted.org/Flask-Security/>`_. This function is
        responsible for associating User models in the database with the
        Security object.

        In case you need to override a Flask-Security form (as is the case
        with implementing CAPTCHA) then you must use super() from within your
        application and provide any arguments destined for Flask-Security.

        >>> def ext_security(self):
        >>>    super(MyApp, self).ext_security(confirm_register_form=CaptchaRegisterForm)
        """

        if not app_models:
            from . import models
        else:
            models = app_models

        user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
        security.init_app(self.app, datastore=user_datastore, **kwargs)
        security._state = self.app.extensions["security"]
        security.datastore = user_datastore

    def database(self):
        """
        Initialize database

        :returns: None

        Flask-Diamond assumes you are modelling your solution using an Entity-
        Relationship framework, and that the application will use a relational
        database (e.g. MySQL, Postgres, or SQlite3) for model persistence.
        Thus, `SQLAlchemy
        <http://docs.sqlalchemy.org/en/rel_0_9/contents.html>`_ and `Flask-
        SQLalchemy <https://pythonhosted.org/Flask-SQLAlchemy/index.html>`_
        are used for database operations.

        Typically, this just works as long as ``SQLALCHEMY_DATABASE_URI`` is
        set correctly in the application configuration.
        """

        db.app = self.app
        db.init_app(self.app)

    def email(self):
        """
        Initialize email facilities.

        :returns: None

        `Flask-Mail <http://pythonhosted.org/Flask-Mail/>`_ is a
        useful tool for creating and sending emails from within a Flask application.
        There are a number of configuration settings beginning with ``MAIL_``
        that permit control over the SMTP credentials used to send email.
        """

        mail.init_app(self.app)

    def wtforms(self):
        """
        WTForms helpers

        :returns: None

        `WTForms <http://wtforms.simplecodes.com/docs/>`_ is a great library
        for using forms and `Flask-WTF <https://flask-
        wtf.readthedocs.org/en/latest/>`_ provides good integration with it.
        WTForms helpers enable you to add custom filters and other custom
        behaviours.
        """

        add_helpers(self.app)

    def debugtoolbar(self):
        """
        Initialize the DebugToolbar

        :returns: None

        The `DebugToolbar <http://flask-
        debugtoolbar.readthedocs.org/en/latest/>`_ is a handy utility for
        debugging your application during development.

        This function obeys the ``DEBUG_TOOLBAR`` configuration setting.  Only
        if this value is explicitly set to True will the Debug Toolbarr run.
        """

        if 'DEBUG_TOOLBAR' in self.app.config and self.app.config['DEBUG_TOOLBAR']:
            toolbar.init_app(self.app)

    def error_handlers(self):
        """
        Initialize handlers for HTTP error events

        :returns: None

        Flask is able to respond to HTTP error codes with custom behaviours.
        By default, it will redirect error 403 (forbidden) to the login page.
        """
        import flask.ext.security as security

        @self.app.errorhandler(403)
        def page_forbidden(e):
            if security.current_user.is_authenticated():
                return flask.redirect(flask.url_for("admin.index"))
            else:
                return flask.redirect(security.url_for_security("login"))

    def request_handlers(self):
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

    def signals(self):
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
            user_role = security.datastore.find_role("User")
            security.datastore.add_role_to_user(extra['user'], user_role)
            self.app.logger.info("added role User to %s" % extra['user'])

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
