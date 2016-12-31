# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

import flask
import datetime
from flask_security import UserMixin
from flask_security.utils import encrypt_password
from flask_marshmallow.fields import fields
from ..facets.database import db
from ..facets.marshalling import ma
from ..mixins.crud import CRUDMixin
from ..mixins.marshmallow import MarshmallowMixin


"A secondary table is used for the one-to-many relationship: User has many Roles"
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class UserSchema(ma.Schema):
    confirmed_at = fields.DateTime(required=False)
    last_login_at = fields.DateTime(required=False)
    current_login_at = fields.DateTime(required=False)

    # RoleSchema must be specified in role.py
    roles = fields.Nested('RoleSchema', allow_none=True, many=True)

    class Meta:
        dateformat = ("%F %T %z")
        additional = (
            "id",
            "email",
            "password",
            "active",
            "last_login_ip",
            "current_login_ip",
            "login_count",
        )


class User(db.Model, UserMixin, CRUDMixin, MarshmallowMixin):
    __schema__ = UserSchema

    id = db.Column(db.Integer, primary_key=True)
    "integer -- primary key"

    email = db.Column(db.String(255), unique=True)
    "string -- email address"

    password = db.Column('password', db.String(255), nullable=False)
    "password -- the users's password"

    active = db.Column(db.Boolean())
    "boolean -- whether the user account is active"

    confirmed_at = db.Column(db.DateTime())
    "datetime -- when the user account was confirmed"

    last_login_at = db.Column(db.DateTime())
    "datetime -- the time of the most recent login"

    current_login_at = db.Column(db.DateTime())
    "datetime -- the time of the current login, if any"

    last_login_ip = db.Column(db.String(255))
    "string -- the IP address of the previous login"

    current_login_ip = db.Column(db.String(255))
    "string -- the IP address of the current login"

    login_count = db.Column(db.Integer(), default=0)
    "integer -- the number of times this account been accessed"

    roles = db.relationship('Role',
        enable_typechecks=False,
        secondary=roles_users,
        # backref=db.backref('users', lazy='dynamic'),
    )

    def __str__(self):
        return self.email

    def confirm(self):
        """
        update a User account so that login is permitted

        :returns: None
        """

        self.confirmed_at = datetime.datetime.now()
        self.active = True
        self.save()

    def add_role(self, role_name):
        """
        update a User account so that it includes a new Role

        :param role_name: the name of the Role to add
        :type role_name: string
        """

        from .. import security

        new_role = security.user_datastore.find_or_create_role(role_name)
        security.user_datastore.add_role_to_user(self, new_role)
        db.session.commit()

    @classmethod
    def register(cls, email, password, confirmed=False, roles=None):
        """
        Create a new user account.

        :param email: the email address used to identify the account
        :type email: string
        :param password: the plaintext password for the account
        :type password: string
        :param confirmed: whether to confirm the account immediately
        :type confirmed: boolean
        :param roles: a list containing the names of the Roles for this User
        :type roles: list(string)
        """

        from .. import security

        new_user = security.user_datastore.create_user(
            email=email,
            password=encrypt_password(password)
        )
        db.session.commit()
        if confirmed:
            new_user.confirm()
        if roles:
            for role_name in roles:
                new_user.add_role(role_name)
        flask.current_app.logger.debug("Created user {0}".format(email))
        return new_user
