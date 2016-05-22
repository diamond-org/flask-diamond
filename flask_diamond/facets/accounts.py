# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from flask.ext.security import SQLAlchemyUserDatastore
from flask.ext.security import Security

security = Security()


def init_accounts(self, user=None, role=None):
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

    # import database
    from .. import db

    if not user or not role:
        raise Exception

    # create datastore
    user_datastore = SQLAlchemyUserDatastore(db, user, role)
    setattr(Security, "user_datastore", user_datastore)
    security.init_app(self.app, datastore=user_datastore)
