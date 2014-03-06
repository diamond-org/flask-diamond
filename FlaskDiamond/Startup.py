# -*- coding: utf-8 -*-

class Startup(object):
    def __init__(self, db, security_obj, toolbar):
        import flask
        self.app = flask.Flask(__name__, static_folder='Views/static', template_folder='Views/templates')
        self.db = db
        self.security_obj = security_obj
        self.toolbar = toolbar

        # configure the application
        self.config()

        # setup database
        self.database()

        # setup components, referring out to our pre-allocated globalish objects
        self.security()
        self.administration()
        self.wtforms()
        self.email()
        self.logger()
        self.blueprints()
        self.debugtoolbar()
        self.signals()
        self.handlers()

    def get_app(self):
        return self.app

    def config(self):
        "Establish configuration"
        self.app.secret_key = None
        self.app.config.from_envvar('SETTINGS')

    def logger(self):
        "init logging"
        import logging
        handler = logging.FileHandler(self.app.config['LOG'])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        self.app.logger.addHandler(handler)
        self.app.logger.setLevel(logging.INFO)
        self.app.logger.debug('Startup with log: %s' % self.app.config['LOG'])

    def blueprints(self):
        "Setup blueprints"
        pass

    def administration(self):
        from . import Administration, Models
        self.admin = Administration.basic_admin(self.app)
        self.admin.add_view(Administration.UserView(Models.User, self.db.session, category="Models"))

    def security(self):
        "Setup Flask-Security"
        from flask.ext.security import SQLAlchemyUserDatastore
        from . import Models

        self.app.config.update(
            SECURITY_POST_LOGIN_VIEW = "/admin",
            SECURITY_PASSWORD_HASH = 'sha256_crypt',
        )

        user_datastore = SQLAlchemyUserDatastore(self.db, Models.User, Models.Role)
        self.security_obj.init_app(self.app, user_datastore)
        self.security_obj.datastore = user_datastore

    def database(self):
        "set up the database"
        self.db.init_app(self.app)

    def email(self):
        "set up flask-mail"
        from flask_mail import Mail

        self.app.config.update(
            MAIL_SERVER = 'localhost',
            MAIL_PORT = 25,
            MAIL_USE_TLS = False,
            MAIL_USERNAME = None,
            MAIL_PASSWORD = None,
        )

        mail = Mail(self.app)
        self.app.mail = mail

    def wtforms(self):
        "WTForms helpers"
        from .Utils.WtfHelpers import add_helpers
        add_helpers(self.app)

    def debugtoolbar(self):
        "Enable the DebugToolbar"
        if 'DEBUG_TOOLBAR' in self.app.config and self.app.config['DEBUG_TOOLBAR']:
            self.toolbar.init_app(self.app)

    def handlers(self):
        import flask
        import flask.ext.security as security

        @self.app.errorhandler(403)
        def page_not_found(e):
            if security.current_user.is_authenticated():
                return flask.redirect(flask.url_for("admin.index"))
            else:
                return flask.redirect(security.url_for_security("login"))

        @self.app.route('/')
        def index():
            "set up the default handler for requests to /"
            return flask.redirect(flask.url_for("admin.index"))

    def signals(self):
        import flask, logging
        from flask.ext.security.signals import user_registered

        @user_registered.connect_via(self.app)
        def user_registered_sighandler(sender, **extra):
            "add User role to all self-registration users"
            user_role = self.security_obj.datastore.find_role("User")
            self.security_obj.datastore.add_role_to_user(extra['user'], user_role)
            logging.getLogger("flask-diamond").info("added role User to %s" % extra['user'])
